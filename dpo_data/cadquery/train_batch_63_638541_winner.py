import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-45))
r=w0.sketch().arc((-40,25),(-63,-89),(36,-39)).arc((90,-24),(33,-8)).arc((28,-3),(22,2)).arc((46,7),(67,20)).segment((88,20)).segment((88,84)).segment((67,84)).arc((24,100),(-17,84)).segment((-40,84)).close().assemble().push([(60,-21)]).circle(17,mode='s').finalize().extrude(90)