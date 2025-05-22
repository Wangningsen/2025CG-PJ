import cadquery as cq
w0=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().segment((-100,-51),(-86,-51)).segment((-84,-93)).segment((12,-88)).arc((-27,-77),(-58,-51)).segment((-27,-51)).arc((74,72),(-39,-40)).segment((-66,-40)).arc((-77,-14),(-81,15)).segment((-89,15)).segment((-86,-40)).segment((-100,-40)).close().assemble().finalize().extrude(-72)