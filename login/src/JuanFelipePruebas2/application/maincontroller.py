class MainController:
    
    def __init__(self):
        pass

    def main_lambda(this, input):
        return {
            'statusCode': 200,
            'body': '¡Hola desde la función Lambda login src 1'
        }
    