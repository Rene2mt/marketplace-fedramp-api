from fastapi import FastAPI, Query, HTTPException
from models import fedramp_data

app = FastAPI(title="FedRAMP Marketplace API",
              description="API for accessing information about cloud service offerings in the FedRAMP marketplace.", version="1.0.0")
# The products list is nested under "data" -> "Products" in the JSON structure
products = fedramp_data["data"]["Products"]


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint with a welcome message."""
    return {"message": "Welcome to the FedRAMP Marketplace API!"}


@app.get("/about")
def about() -> dict[str, str]:
    """About endpoint describing the API."""
    return {
        "message": (
            "This API can be used to get information about cloud service offerings (CSOs) "
            "from the FedRAMP marketplace."
        )
    }


@app.get("/products/")
def product_items(
    skip: int = Query(0, ge=0, description="Number of products to skip"),
    limit: int = Query(
        50, ge=1, le=100, description="Number of products to return"),
) -> dict[str, list]:
    """
    List products with pagination.
    - skip: Number of products to skip.
    - limit: Number of products to return (max 100).
    """
    return {"products": products[skip: skip + limit]}


@app.get("/products/{product_id}")
def get_product_by_id(product_id: str) -> dict:
    """
    Get a product by its ID.
    - product_id: The ID of the product.
    """
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/products/{product_id}/status")
def get_product_status(product_id: str) -> dict:
    """
    Get the status of a product by its ID.
    - product_id: The ID of the product.
    """
    for product in products:
        if product["id"] == product_id:
            return {"status": product.get("status")}
    raise HTTPException(status_code=404, detail="Product not found")
