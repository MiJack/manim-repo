#!/usr/bin/env python

from manimlib.imports import *


# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)



# See old_projects folder for many, many more
NORMAL = 0
START = 1
END = 2


class FSM_STATUS(VGroup):
    def __init__(self, txt, radius=0.5, node_types=[NORMAL], **kwargs):
        # if not all([isinstance(m, VMobject) for m in vmobjects]):
        #     raise Exception("All submobjects must be of type VMobject")
        VMobject.__init__(self, **kwargs)
        self.radius = radius
        self.circle = Circle(radius=self.radius)
        if END in node_types:
            self.add(Circle(radius=self.radius * 0.8))
        if START in node_types:
            self.start_line = Vector()
            self.start_line.next_to(self.circle, LEFT)
            self.add(self.start_line)

        self.add(self.circle)
        self.example_text = TexMobject(
            txt,
            tex_to_color_map={"text": YELLOW}
        )
        self.add(self.example_text)

    def getCirclePoint(self, angle=0, color="BLUE"):
        center_value = self.circle.get_center();
        arc = (angle) / 180 * PI
        return center_value + LEFT * np.cos(arc) * self.radius + UP * np.sin(arc) * self.radius


class FSM(Scene):
    def construct(self):
        #  以1结尾字符串 .*1
        #  create status
        status_1 = self.get_status("s_0", node_types=[START]);
        status_2 = self.get_status("s_1", node_types=[END]);
        # position status node
        status_1.move_to(LEFT * 3)
        status_2.move_to(RIGHT * 3)

        status_1_to_status_1_curved_arrow_by_0 = CurvedArrow(start_point=status_1.getCirclePoint(60),
                                                             end_point=status_1.getCirclePoint(120), angle=-3 * TAU / 4)
        status_1_to_status_1_curved_arrow_by_0_txt = TextMobject("0");
        status_1_to_status_1_curved_arrow_by_0_txt.next_to(status_1_to_status_1_curved_arrow_by_0, TOP)
        self.play(ShowCreation(status_1_to_status_1_curved_arrow_by_0),
                  ShowCreation(status_1_to_status_1_curved_arrow_by_0_txt))

        status_1_to_status_2_curved_arrow_by_1 = CurvedArrow(start_point=status_1.getCirclePoint(150),
                                                             end_point=status_2.getCirclePoint(30), angle=- TAU / 4)

        status_1_to_status_2_curved_arrow_by_1_txt = TextMobject("1");
        status_1_to_status_2_curved_arrow_by_1_txt.next_to(status_1_to_status_2_curved_arrow_by_1, TOP)
        self.play(ShowCreation(status_1_to_status_2_curved_arrow_by_1),
                  ShowCreation(status_1_to_status_2_curved_arrow_by_1_txt))

        status_2_to_status_1_curved_arrow_by_0 = CurvedArrow(start_point=status_2.getCirclePoint(-30),
                                                             end_point=status_1.getCirclePoint(-150), angle=- TAU / 4)

        status_2_to_status_1_curved_arrow_by_0_txt = TextMobject("0");
        status_2_to_status_1_curved_arrow_by_0_txt.next_to(status_2_to_status_1_curved_arrow_by_0, BOTTOM)
        self.play(ShowCreation(status_2_to_status_1_curved_arrow_by_0),
                  ShowCreation(status_2_to_status_1_curved_arrow_by_0_txt))

        status_2_to_status_2_curved_arrow_by_1 = CurvedArrow(start_point=status_2.getCirclePoint(60),
                                                             end_point=status_2.getCirclePoint(120), angle=-3 * TAU / 4)
        status_2_to_status_2_curved_arrow_by_1_txt = TextMobject("1");
        status_2_to_status_2_curved_arrow_by_1_txt.next_to(status_2_to_status_2_curved_arrow_by_1, TOP)
        self.play(ShowCreation(status_2_to_status_2_curved_arrow_by_1),
                  ShowCreation(status_2_to_status_2_curved_arrow_by_1_txt))

        self.wait(duration=4)

    def get_status(self, txt, node_types=[NORMAL]):
        node = FSM_STATUS(txt, node_types=node_types)
        self.add(node)
        return node
