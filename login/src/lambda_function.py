from application.maincontroller import MainController


def lambda_handler(event, context):
    main = MainController()
    return main.main_lambda(event)