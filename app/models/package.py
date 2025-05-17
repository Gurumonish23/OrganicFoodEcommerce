from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.dependencies.database import Base

# Association table for many-to-many relationship between packages and products
package_product_association = Table(
    'package_product_association',
    Base.metadata,
    Column('package_id', Integer, ForeignKey('packages.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    products = relationship("Product", secondary=package_product_association, back_populates="packages")
    orders = relationship("Order", back_populates="package")

# Assuming a Product model exists with a relationship to Package
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    packages = relationship("Package", secondary=package_product_association, back_populates="products")