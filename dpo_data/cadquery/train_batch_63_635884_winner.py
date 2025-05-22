import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().segment((-48,-22),(-32,-100)).segment((37,-85)).segment((22,-14)).arc((22,55),(-12,-5)).segment((-1,-13)).close().assemble().push([(-1.5,38)]).rect(23,10,mode='s').push([(-6,-54)]).circle(6,mode='s').push([(30.5,81.5)]).rect(7,37).finalize().extrude(68)