import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().arc((73,-49),(89,-22),(73,5)).close().assemble().finalize().extrude(-9).union(w0.sketch().arc((53,47),(64,-20),(56,48)).close().assemble().push([(59,14)]).circle(28,mode='s').finalize().extrude(31)).union(w1.sketch().segment((-47,-66),(-22,-66)).arc((39,-90),(14,-29)).arc((14,-25),(13,-21)).segment((13,3)).segment((-47,3)).segment((-47,-21)).arc((-49,-32),(-47,-42)).close().assemble().finalize().extrude(45))