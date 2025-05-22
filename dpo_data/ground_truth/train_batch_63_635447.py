import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
r=w0.sketch().segment((-98,-9),(-92,-16)).segment((-97,-25)).segment((-73,-36)).segment((-14,-100)).segment((12,-75)).segment((47,-91)).segment((69,-41)).arc((30,3),(58,55)).segment((17,100)).segment((-9,75)).segment((-44,91)).segment((-83,6)).close().assemble().push([(81,9)]).circle(17).finalize().extrude(27)