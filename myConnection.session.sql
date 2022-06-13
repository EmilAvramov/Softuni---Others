

CREATE TABLE order_items (
    order_id INT(11) NOT NULL,
    item_id INT(11) NOT NULL,
    CONSTRAINT pk_order_items PRIMARY KEY (order_id, item_id),
    CONSTRAINT fk_order_ids FOREIGN KEY (order_id) REFERENCES orders (order_id),
    CONSTRAINT fk_items FOREIGN KEY (item_id) REFERENCES items (item_id)
);