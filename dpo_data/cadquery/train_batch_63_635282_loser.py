import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().push([(-69,44)]).circle(31).circle(19,mode='s').push([(9.5,23)]).rect(31,8).push([(10,23)]).circle(2,mode='s').finalize().extrude(64).union(w1.sketch().arc((-65,23),(-17,-50),(-15,37)).arc((-44,51),(-65,23)).assemble().finalize().extrude(80))