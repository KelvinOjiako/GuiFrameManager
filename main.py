from FrameManager.GuiTestManager import experimental_main, move_to_previous_widget, move_to_next_widget
from guizero import App, PushButton


def sample_gui_test():
    app = App(title="Preserve the Nerve Sample Project")
    manager = experimental_main(app)
    manager.activate_current_element()
    previous_button = PushButton(app, text="prev", command=move_to_previous_widget, args=[manager])
    next_button = PushButton(app, text="next", command=move_to_next_widget, args=[manager])
    app.display()


if __name__ == '__main__':
    sample_gui_test()
