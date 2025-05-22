import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((-58,-30),(-56,-33)).arc((-51,-67),(-29,-92)).segment((-30,-92)).segment((-12,-100)).segment((-12,-34)).segment((57,-34)).arc((53,-20),(45,-7)).segment((46,-7)).segment((38,3)).segment((37,3)).arc((-12,12),(-52,-23)).close().assemble().push([(37,79)]).circle(21).finalize().extrude(24)