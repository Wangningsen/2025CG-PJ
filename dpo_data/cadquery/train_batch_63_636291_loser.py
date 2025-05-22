import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
w1=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((49,16),(59,16)).arc((49,54),(71,17)).segment((71,27)).arc((68,52),(49,35)).close().assemble().finalize().extrude(133).union(w1.sketch().push([(-57,-33)]).circle(25).push([(-57,-33.5)]).rect(40,19,mode='s').finalize().extrude(-88))