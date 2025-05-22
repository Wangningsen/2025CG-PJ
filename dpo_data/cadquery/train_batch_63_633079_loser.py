import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
w1=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().push([(12,55)]).circle(15).push([(12,54.5)]).rect(18,9,mode='s').finalize().extrude(-65).union(w0.workplane(offset=45/2).moveTo(-28,-51).box(86,98,45)).union(w0.workplane(offset=88/2).moveTo(69,-53).box(4,72,88)).union(w1.sketch().push([(-77.5,3)]).rect(23,90).push([(-77,3)]).circle(4,mode='s').finalize().extrude(63))