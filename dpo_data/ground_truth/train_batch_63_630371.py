import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.sketch().arc((-13,10),(-38,-9),(-8,-22)).arc((100,8),(-13,10)).assemble().finalize().extrude(-95).union(w0.sketch().arc((-50,-5),(-96,-43),(-46,-9)).segment((15,-9)).segment((15,-5)).close().assemble().push([(-72,-25)]).circle(23,mode='s').finalize().extrude(20))