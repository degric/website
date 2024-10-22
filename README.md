---

# Mieleria 

## Base de Datos

### Tablas: 
- productos
    - id 
    - nombre
    - precio
    - stock
    - descripcion

```sql
CREATE TABLE productos (
    id int auto-increment primary key,
    name varchar(100),
    precio decimal(6,3) not null,
    stock int not null, 
    descripcion varchar(500) not null
);
```
