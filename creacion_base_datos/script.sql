-- Tabla de Clientes

CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY
                       UNIQUE,
    nombre     TEXT    NOT NULL,
    apellido   TEXT    NOT NULL,
    telefono   TEXT
);

-- Tabla de Compras

CREATE TABLE compra (
    id_compra    INTEGER PRIMARY KEY
                         UNIQUE,
    fk_cliente   INTEGER REFERENCES cliente (id_cliente),
    fecha_compra TEXT    NOT NULL,
    total        REAL    NOT NULL
);

-- Tabla de Detalle de Compras

CREATE TABLE detalle_compras (
    id_detalle_compra INTEGER PRIMARY KEY
                              UNIQUE,
    fk_compra         INTEGER REFERENCES compra (id_compra),
    fk_producto       INTEGER REFERENCES productos (id_producto) 
);

-- Tabla de Productos

CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY
                        UNIQUE,
    nombre      TEXT    NOT NULL,
    precio      REAL    NOT NULL,
    stock       INTEGER NOT NULL
);

-- Tabla de Pedidos

CREATE TABLE pedidos (
    id_pedido    INTEGER PRIMARY KEY
                         UNIQUE,
    fk_producto  INTEGER REFERENCES productos (id_producto),
    fecha_pedido TEXT    NOT NULL,
    total        INTEGER NOT NULL,
    estado       TEXT    CHECK (estado IN ('Pendiente', 'Enviado', 'Entregado') ) 
                         NOT NULL
);

-- Tabla de Detalle de Pedidos

CREATE TABLE detalle_pedidos (
    id_detalle      INTEGER PRIMARY KEY
                            UNIQUE,
    fk_pedido       INTEGER REFERENCES pedidos (id_pedido),
    producto        TEXT    NOT NULL,
    cantidad        INTEGER CHECK (cantidad > 0),
    precio_unitario REAL    NOT NULL
);

-- Tabla de Ventas

CREATE TABLE ventas (
    id_venta    INTEGER PRIMARY KEY
                        UNIQUE,
    fk_empleado INTEGER REFERENCES empleados (id_empleado),
    fk_cliente  INTEGER REFERENCES cliente (id_cliente),
    fecha_venta TEXT    NOT NULL
                        DEFAULT CURRENT_DATE
);



-- Tabla de Detalle de Ventas

CREATE TABLE ventas (
    id_venta    INTEGER PRIMARY KEY
                        UNIQUE,
    fk_empleado INTEGER REFERENCES empleados (id_empleado),
    fk_cliente  INTEGER REFERENCES cliente (id_cliente),
    fecha_venta TEXT    NOT NULL
                        DEFAULT CURRENT_DATE,
    total       REAL    NOT NULL
);

-- Tabla de Empleados

CREATE TABLE empleados (
    id_empleado INTEGER PRIMARY KEY
                        UNIQUE,
    nombre      TEXT    NOT NULL,
    apellido    TEXT    NOT NULL,
    cargo       TEXT    NOT NULL,
    salario     REAL    NOT NULL
);


-- Tabla de Proveedores

CREATE TABLE proveedor (
    id_proveedor      INTEGER PRIMARY KEY
                              UNIQUE,
    fk_detalle_pedido INTEGER REFERENCES detalle_pedidos (id_detalle),
    nombre            TEXT    NOT NULL,
    direccion         TEXT    NOT NULL,
    telefono          TEXT    NOT NULL
);

-- Tabla de Departamento

CREATE TABLE departamento (
    id_departamento INTEGER PRIMARY KEY
                            UNIQUE,
    nombre          TEXT    NOT NULL,
    fk_empleado     INTEGER REFERENCES empleados (id_empleado) 
);

