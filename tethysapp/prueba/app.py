from tethys_sdk.base import TethysAppBase


class Prueba(TethysAppBase):
    """
    Tethys app class for Prueba.
    """

    name = 'Prueba'
    description = ''
    package = 'prueba'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'prueba'
    color = '#273c75'
    tags = ''
    enable_feedback = False
    feedback_emails = []