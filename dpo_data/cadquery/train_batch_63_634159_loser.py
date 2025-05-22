import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-88))
r=w0.sketch().segment((-57,-100),(57,-100)).segment((57,100)).segment((28,100)).arc((47,80),(51,52)).arc((50,46),(45,41)).arc((13,13),(-28,25)).arc((-44,58),(-21,89)).arc((-23,95),(-22,100)).segment((-57,100)).close().assemble().push([(50,-32)]).circle(3,mode='s').finalize().extrude(176)