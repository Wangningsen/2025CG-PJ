import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,56))
r=w0.sketch().push([(-28.5,-92)]).rect(133,16).push([(-29,-92)]).circle(8,mode='s').reset().face(w0.sketch().arc((55,85),(-52,-63),(63,79)).arc((45,66),(55,85)).assemble()).finalize().extrude(-111)