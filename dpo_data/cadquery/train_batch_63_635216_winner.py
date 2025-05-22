import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().segment((-41,-100),(31,-100)).segment((31,-17)).segment((-22,-17)).arc((-28,-1),(-30,-17)).segment((-41,-17)).close().assemble().finalize().extrude(-65).union(w0.sketch().push([(-13,58)]).circle(42).push([(-13.5,58.5)]).rect(75,29,mode='s').finalize().extrude(9)).union(w1.sketch().arc((52,-38),(53,-37),(55,-38)).segment((55,-35)).segment((52,-35)).close().assemble().finalize().extrude(-65))