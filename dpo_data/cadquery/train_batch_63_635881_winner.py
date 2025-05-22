import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
w1=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().segment((61,-9),(100,-9)).segment((100,85)).segment((96,85)).arc((90,88),(84,85)).segment((61,85)).close().assemble().finalize().extrude(-79).union(w0.sketch().segment((17,-88),(58,-88)).arc((38,-59),(17,-88)).assemble().finalize().extrude(-59)).union(w0.sketch().push([(-51.5,74)]).rect(97,24).push([(-52,74)]).circle(10,mode='s').finalize().extrude(49)).union(w1.workplane(offset=-53/2).moveTo(-3,-3.5).box(24,29,53))