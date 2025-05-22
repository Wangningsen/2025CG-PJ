import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-13,-38),(13,-38)).segment((13,-32)).arc((0,-20),(22,-12)).arc((24,9),(13,24)).segment((13,38)).segment((-13,38)).segment((-13,24)).arc((-25,0),(-13,-21)).close().assemble().finalize().extrude(200)