ambientes = [
    'Cocina', 'Comedor', 'Cochera', 'Quincho', 'Baño 1', 'Baño 2',
    'Habitación 1', 'Habitación 2', 'Sala de estar', 'Terraza', 'Patio'
]

conexiones = [
    ('Cocina', 'Comedor', 4),
    ('Comedor', 'Cochera', 9),
    ('Cochera', 'Quincho', 7),
    ('Quincho', 'Baño 1', 6),
    ('Baño 1', 'Baño 2', 5),
    ('Baño 2', 'Habitación 1', 4),
    ('Habitación 1', 'Habitación 2', 5),
    ('Habitación 2', 'Sala de estar', 8),
    ('Sala de estar', 'Terraza', 7),
    ('Terraza', 'Patio', 6),
    ('Patio', 'Cocina', 8),
    ('Cocina', 'Cochera', 10),
    ('Comedor', 'Quincho', 11),
    ('Cochera', 'Baño 1', 12),
    ('Quincho', 'Baño 2', 8),
    ('Baño 1', 'Habitación 1', 7),
    ('Baño 2', 'Habitación 2', 9),
    ('Habitación 1', 'Sala de estar', 11),
    ('Habitación 2', 'Terraza', 10),
    ('Sala de estar', 'Patio', 9),
    ('Terraza', 'Cocina', 12),
    ('Patio', 'Comedor', 10),
    ('Cocina', 'Sala de estar', 13),
]
