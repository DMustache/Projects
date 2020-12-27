import glooey
import pyglet

pyglet.font.add_file('Lato-Regular.ttf')
pyglet.font.load('Lato Regular')

class WesnothLabel(glooey.Label):
    custom_font_name = 'Lato Regular'
    custom_font_size = 10
    custom_color = '#b9ad86'
    custom_alignment = 'center'

class WesnothBorder(glooey.Background):
    custom_center = pyglet.resource.texture('center.png')
    custom_top = pyglet.resource.texture('top.png')
    custom_bottom = pyglet.resource.texture('bottom.png')
    custom_left = pyglet.resource.texture('left.png')
    custom_right = pyglet.resource.texture('right.png')
    custom_top_left = pyglet.resource.image('top_left.png')
    custom_top_right = pyglet.resource.image('top_right.png')
    custom_bottom_left = pyglet.resource.image('bottom_left.png')
    custom_bottom_right = pyglet.resource.image('bottom_right.png')
# main style

class WesnothScrollBox(glooey.ScrollBox):
    custom_alignment = 'top right'
    custom_height_hint = 200

    class Frame(glooey.Frame):

        class Decoration(glooey.Background):
            custom_center = pyglet.resource.texture('center.png')

        class Box(glooey.Bin):
            custom_horz_padding = 2

    class VBar(glooey.VScrollBar):
        custom_scale_grip = True

        class Decoration(glooey.Background):
            custom_top = pyglet.resource.image('bar_top.png')
            custom_center = pyglet.resource.texture('bar_vert.png')
            custom_bottom = pyglet.resource.image('bar_bottom.png')
            custom_vert_padding = 25

        class Forward(glooey.Button):
            custom_base_image = pyglet.resource.image('forward_base.png')
            custom_over_image = pyglet.resource.image('forward_over.png')
            custom_down_image = pyglet.resource.image('forward_down.png')

        class Backward(glooey.Button):
            custom_base_image = pyglet.resource.image('backward_base.png')
            custom_over_image = pyglet.resource.image('backward_over.png')
            custom_down_image = pyglet.resource.image('backward_down.png')

        class Grip(glooey.Button):
            custom_height_hint = 20
            custom_alignment = 'fill'

            custom_base_top = pyglet.resource.image('grip_top_base.png')
            custom_base_center = pyglet.resource.texture('grip_vert_base.png')
            custom_base_bottom = pyglet.resource.image('grip_bottom_base.png')

            custom_over_top = pyglet.resource.image('grip_top_over.png')
            custom_over_center = pyglet.resource.texture('grip_vert_over.png')
            custom_over_bottom = pyglet.resource.image('grip_bottom_over.png')

            custom_down_top = pyglet.resource.image('grip_top_down.png')
            custom_down_center = pyglet.resource.texture('grip_vert_down.png')
            custom_down_bottom = pyglet.resource.image('grip_bottom_down.png')

class WesnothLoremIpsum(glooey.LoremIpsum):
    custom_font_name = 'Lato Regular'
    custom_font_size = 10
    custom_color = '#b9ad86'
    custom_alignment = 'fill horz'
# WesnothLoremIpsum & WesnothLoremIpsum

class WesnothCheckbox(glooey.Checkbox):
    custom_checked_base = pyglet.resource.image('checked_base.png')
    custom_checked_over = pyglet.resource.image('checked_over.png')
    custom_checked_down = pyglet.resource.image('unchecked_down.png')
    custom_unchecked_base = pyglet.resource.image('unchecked_base.png')
    custom_unchecked_over = pyglet.resource.image('unchecked_over.png')
    custom_unchecked_down = pyglet.resource.image('unchecked_down.png')

class WesnothLabeledCheckbox(glooey.Widget):
    Label = WesnothLabel
    Checkbox = WesnothCheckbox
    custom_alignment = 'center'

    class HBox(glooey.HBox):
        custom_padding = 6

    def __init__(self, text):
        super().__init__()

        hbox = self.HBox()
        self.checkbox = self.Checkbox()
        self.label = self.Label(text)

        hbox.pack(self.checkbox)
        hbox.add(self.label)

        # Configure `checkbox` to respond to clicks anywhere in `hbox`.
        self.checkbox.add_proxy(hbox, exclusive=True)

        # Make the `on_toggle` events appear to come from this widget.
        self.relay_events_from(self.checkbox, 'on_toggle')

        self._attach_child(hbox)

    def toggle(self):
        self.checkbox.toggle()

    def check(self):
        self.checkbox.check()

    def uncheck(self):
        self.checkbox.uncheck()

    @property
    def is_checked(self):
        return self.checkbox.is_checked
WesnothLabeledCheckbox.register_event_type('on_toggle')
# WesnothCheckBox

class WesnothButton(glooey.Button):
    Foreground = WesnothLabel

    class Base(glooey.Image):
        custom_image = pyglet.resource.image('base.png')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('over.png')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('down.png')
# WesnothButton

class WesnothDialog(glooey.YesNoDialog):
    class Decoration(glooey.Background):
        custom_center = pyglet.resource.texture('center.png')
        custom_top = pyglet.resource.texture('top.png')
        custom_bottom = pyglet.resource.texture('bottom.png')
        custom_left = pyglet.resource.texture('left.png')
        custom_right = pyglet.resource.texture('right.png')
        custom_top_left = pyglet.resource.image('top_left.png')
        custom_top_right = pyglet.resource.image('top_right.png')
        custom_bottom_left = pyglet.resource.image('bottom_left.png')
        custom_bottom_right = pyglet.resource.image('bottom_right.png')

    class Box(glooey.Grid):
        custom_right_padding = 14
        custom_top_padding = 14
        custom_left_padding = 17
        custom_bottom_padding = 17
        custom_cell_padding = 9

    class Buttons(glooey.HBox):
        custom_cell_padding = 3
        custom_alignment = 'right'

    class YesButton(WesnothButton):
        custom_text = 'Ok'

    class NoButton(WesnothButton):
        custom_text = 'No'
# WesnothDialog

class WesnothForm(glooey.Form):
    custom_alignment = 'top left'
    custom_top_padding = 30
    custom_left_padding = 30

    class Label(glooey.EditableLabel):
        custom_font_name = 'Lato Regular'
        custom_font_size = 10
        custom_color = '#b9ad86'
        custom_horz_padding = 5
        custom_top_padding = 5
        custom_width_hint = 200

    class Base(glooey.Background):
        custom_center = pyglet.resource.texture('form_center.png')
        custom_left = pyglet.resource.image('form_left.png')
        custom_right = pyglet.resource.image('form_right.png')
# WesnothForm

window = pyglet.window.Window()
gui = glooey.Gui(window)

border = WesnothBorder()
gui.add(border)

scroll = WesnothScrollBox()
scroll.add(WesnothLoremIpsum())
scroll.alignment = 'top right'
gui.add(scroll)
scroll.push_handlers(
    on_mouse_scroll=lambda x, y, scroll_x, scroll_y:
        print(f'{scroll} mouse scrolled {x} {y} {scroll_x} {scroll_y}'),
    on_click=lambda scroll:
        print(f'{scroll} was clicked'),
    on_mouse_drag=lambda x, y, dx, dy, buttons, modifires:
        print(f'{scroll} {x} {y} {dx} {dy} {buttons} {modifires}'))

button = WesnothButton('Button')
button.alignment = 'top left'
gui.add(button)
button.push_handlers(on_click=lambda button: print(f'{button} was clicked'))

checkbox = WesnothLabeledCheckbox('Toggle something')
checkbox.alignment = 'bottom left'
gui.add(checkbox)
checkbox.push_handlers(on_toggle=lambda w:
        print(f"{w} {'checked' if w.is_checked else 'unchecked'}"))

form = WesnothForm()
gui.add(form)
form.push_handlers(on_unfocus=lambda w:print(f"Form input: '{w.text}'"))

dialog = WesnothDialog()
WesnothLabel.custom_alignment = 'top left'
WesnothLabel.custom_top_padding = 14
WesnothLabel.custom_right_padding = 17
WesnothLabel.custom_left_padding = 17
dialog.add(WesnothLabel('Буиш Учиться? Если нет, то дам по жопе и отключу интернет', line_wrap=200))
dialog.size_hint = 300, 100
dialog.open(gui)
dialog.push_handlers(on_click=lambda dialog: print(f'{dialog} clicked'))

pyglet.app.run()