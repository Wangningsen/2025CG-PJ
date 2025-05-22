import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
r=w0.sketch().arc((-71,85),(-34,-79),(100,24)).segment((59,5)).arc((45,-25),(16,-43)).segment((16,-82)).segment((-16,-82)).segment((-16,-43)).arc((-55,-8),(-52,44)).close().assemble().finalize().extrude(116)