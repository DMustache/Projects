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

class BlueRectangle(glooey.Widget):
    custom_alignment = 'center'
    custom_size_hint = 300, 200

    def __init__(self):
        super().__init__()
        self.vertex_list = None

    def do_claim(self):
        return 0, 0

    def do_draw(self):
        vertices = (
                self.rect.bottom_left.tuple +
                self.rect.bottom_right.tuple +
                self.rect.top_right.tuple +
                self.rect.top_left.tuple
        )
        blue = 1, 71, 108

        if self.vertex_list is None:
            self.vertex_list = self.batch.add(
                    4, pyglet.gl.GL_QUADS, self.group,
                    ('v2f', vertices), ('c3B', 4 * blue)
            )
        else:
            self.vertex_list.vertices = vertices

    def do_undraw(self):
        if self.vertex_list is not None:
            self.vertex_list.delete()
            self.vertex_list = None
# BlueRectangle

class SpriteDemo(glooey.Widget):
    custom_alignment = 'center'

    def __init__(self):
        super().__init__()
        self.sprite = None

    def do_claim(self):
        return 200, 200

    def do_regroup(self):
        if self.sprite is not None:
            self.sprite.batch = self.batch
            self.sprite.group = self.group

    def do_draw(self):
        if self.sprite is None:
            self.sprite = pyglet.sprite.Sprite(
                    img=pyglet.image.load('wesnoth_logo.png'),
                    x=self.rect.left,
                    y=self.rect.bottom,
                    batch=self.batch,
                    group=self.group,
            )
        else:
            self.sprite.set_position(
                    x=self.rect.left,
                    y=self.rect.bottom,
            )

    def do_undraw(self):
        if self.sprite is not None:
            self.sprite.delete()
            self.sprite = None
# SpiritDemo

window = pyglet.window.Window()
gui = glooey.Gui(window)

border = WesnothBorder()
gui.add(border)

demo = BlueRectangle()
gui.add(demo)
gui.push_handlers(on_click=lambda w: demo.unhide() if demo.is_hidden else demo.hide())

dlogo = SpriteDemo()
gui.add(dlogo)

scroll = WesnothScrollBox()
scroll.add(WesnothLoremIpsum())
scroll.alignment = 'top right'
gui.add(scroll)

button = WesnothButton('Button')
button.alignment = 'top left'
gui.add(button)

checkbox = WesnothLabeledCheckbox('Toggle something')
checkbox.alignment = 'bottom left'
gui.add(checkbox)

form = WesnothForm()
gui.add(form)

dialog = WesnothDialog()
WesnothLabel.custom_alignment = 'top left'
WesnothLabel.custom_top_padding = 14
WesnothLabel.custom_right_padding = 17
WesnothLabel.custom_left_padding = 17
dialog.add(WesnothLabel('Буиш Учиться? Если нет, то дам по жопе и отключу интернет', line_wrap=200))
dialog.size_hint = 300, 100
dialog.open(gui)



pyglet.app.run()