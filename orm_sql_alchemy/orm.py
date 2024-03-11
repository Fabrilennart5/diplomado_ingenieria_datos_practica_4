from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, CheckConstraint
from sqlalchemy import create_engine, func
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Tabla de Clientes
class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    telefono = Column(String(255))


# Tabla de Compras
class Compra(Base):
    __tablename__ = "compra"
    id_compra = Column(Integer, primary_key=True, unique=True)
    fk_cliente = Column(Integer, ForeignKey("cliente.id_cliente"))
    fecha_compra = Column(Text, nullable=False)
    total = Column(Float, nullable=False)


# Tabla de Detalle de Compras
class DetalleCompra(Base):
    __tablename__ = "detalle_compra"
    id_detalle_compra = Column(Integer, primary_key=True, unique=True)
    fk_compra = Column(Integer, ForeignKey("compra.id_compra"))
    fk_producto = Column(Integer, ForeignKey("productos.id_producto"))


# Tabla de Productos
class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)


# Tabla de Pedidos
class Pedido(Base):
    __tablename__ = "pedidos"
    id_pedido = Column(Integer, primary_key=True, unique=True)
    fk_producto = Column(Integer, ForeignKey("productos.id_producto"))
    fecha_pedido = Column(Text, nullable=False)
    total = Column(Integer, nullable=False)
    estado = Column(String(255), nullable=False)
    __table_args__ = (
        CheckConstraint(estado.in_(["Pendiente", "Enviado", "Entregado"])),
    )


# Tabla de Detalle de Pedidos
class DetallePedido(Base):
    __tablename__ = "detalle_pedidos"
    id_detalle = Column(Integer, primary_key=True, unique=True, nullable=False)
    fk_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"))
    producto = Column(String(255), nullable=False)
    cantidad = Column(
        Integer, CheckConstraint("cantidad > 0")
    )  # Corrected constraint syntax
    precio_unitario = Column(Float, nullable=False)


# Tabla de Ventas
class Venta(Base):
    __tablename__ = "ventas"
    id_venta = Column(Integer, primary_key=True, unique=True)
    fk_empleado = Column(Integer, ForeignKey("empleados.id_empleado"))
    fk_cliente = Column(Integer, ForeignKey("cliente.id_cliente"))
    fecha_venta = Column(Text, nullable=False, default=func.current_timestamp())
    total = Column(Float, nullable=False)


# Tabla de Empleados
class Empleado(Base):
    __tablename__ = "empleados"
    id_empleado = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    cargo = Column(String(255), nullable=False)
    salario = Column(Float, nullable=False)


# Tabla de Proveedores
class Proveedor(Base):
    __tablename__ = "proveedor"
    id_proveedor = Column(Integer, primary_key=True, unique=True)
    fk_detalle_pedido = Column(Integer, ForeignKey("detalle_pedidos.id_detalle"))
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    telefono = Column(String(255), nullable=False)


# Tabla de Departamento
class Departamento(Base):
    __tablename__ = "departamento"
    id_departamento = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False)
    fk_empleado = Column(Integer, ForeignKey("empleados.id_empleado"))


# Relaciones entre las entidades
Cliente.compras = relationship("Compra", backref="cliente")
Compra.detalle_compras = relationship("DetalleCompra", backref="compra")
Producto.detalle_pedidos = relationship("DetallePedido", backref="producto")
Pedido.detalle_pedidos = relationship("DetallePedido", backref="pedido")
Venta.cliente = relationship("Cliente", backref="ventas")
Venta.empleado = relationship("Empleado", backref="ventas")
Proveedor.detalle_pedidos = relationship("DetallePedido", backref="proveedor")
Departamento.empleado = relationship("Empleado", backref="departamentos")

# Crear la Base de datos
engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
