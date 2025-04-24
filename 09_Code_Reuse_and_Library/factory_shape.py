class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return "Ini Adalah Lingkaran"
        elif shape_type == "square":
            return "Ini Adalah Persegi"
        elif shape_type == "rectangle":
            return "Ini Adalah Persegi Panjang"
        else:
            raise ValueError("Unknown shape type")
        
print(ShapeFactory.get_shape("circle"))