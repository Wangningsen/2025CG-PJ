import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().segment((-100,-73),(-17,-73)).segment((9,-96)).segment((30,-67)).arc((34,-65),(38,-62)).segment((73,-65)).segment((77,2)).segment((100,33)).segment((79,48)).segment((81,58)).segment((60,59)).segment((14,96)).segment((5,85)).arc((1,85),(-2,87)).segment((-100,87)).close().assemble().finalize().extrude(18)