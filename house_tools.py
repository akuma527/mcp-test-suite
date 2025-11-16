# Tool schemas for each agent

PAINTER_TOOLS = [
    {
        "name": "apply_paint",
        "description": "Apply paint to a surface",
        "parameters": [
            {"name": "surface", "type": "string", "description": "Surface to paint"}
        ]
    },
    {
        "name": "fill_bucket",
        "description": "Fill a bucket with paint",
        "parameters": [
            {"name": "color", "type": "string", "description": "Color of paint"}
        ]
    }
]

CARPENTER_TOOLS = [
    {
        "name": "cut_wood",
        "description": "Cut wood to size",
        "parameters": [
            {"name": "size", "type": "string", "description": "Size to cut wood to"}
        ]
    },
    {
        "name": "join_wood",
        "description": "Join pieces of wood",
        "parameters": [
            {"name": "pieces", "type": "string", "description": "Pieces to join"}
        ]
    }
]

MASON_TOOLS = [
    {
        "name": "apply_cement",
        "description": "Apply cement to a surface",
        "parameters": [
            {"name": "surface", "type": "string", "description": "Surface to apply cement to"}
        ]
    },
    {
        "name": "apply_brick",
        "description": "Apply brick to a surface",
        "parameters": [
            {"name": "surface", "type": "string", "description": "Surface to apply brick to"}
        ]
    }
]
