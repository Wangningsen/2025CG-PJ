import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.sketch().segment((-86,-89),(-45,-89)).arc((0,-100),(45,-89)).segment((86,-89)).segment((86,-51)).arc((100,0),(86,51)).segment((86,89)).segment((45,89)).arc((0,100),(-45,89)).segment((-86,89)).segment((-86,51)).arc((-100,0),(-86,-51)).close().assemble().finalize().extrude(-137)