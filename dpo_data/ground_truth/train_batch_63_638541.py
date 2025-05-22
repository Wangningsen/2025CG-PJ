import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,45))
r=w0.sketch().arc((-40,25),(-68,-85),(36,-39)).arc((90,-15),(31,-12)).arc((27,-4),(21,4)).arc((42,7),(60,20)).segment((88,20)).segment((88,84)).segment((60,84)).arc((24,100),(-12,84)).segment((-40,84)).close().assemble().push([(60,-21)]).circle(17,mode='s').finalize().extrude(-90)