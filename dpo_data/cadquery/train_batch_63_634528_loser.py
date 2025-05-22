import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
r=w0.sketch().arc((-71,85),(-40,-77),(100,24)).arc((79,14),(59,5)).arc((55,-8),(47,-22)).segment((47,-26)).segment((44,-26)).arc((30,-37),(16,-43)).segment((16,-82)).segment((-16,-82)).segment((-16,-43)).arc((-51,-17),(-59,26)).arc((-61,63),(-71,85)).assemble().finalize().extrude(116)