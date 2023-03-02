from FrameManager.GuiTestManager import experimental_main
from guizero import App


def sample_gui_test():
    app = App(title="Preserve the Nerve Sample Project")
    manager = experimental_main(app)


if __name__ == '__main__':
    sample_gui_test()
