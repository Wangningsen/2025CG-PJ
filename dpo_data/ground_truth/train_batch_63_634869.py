import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
r=w0.sketch().rect(152,200).rect(98,130,mode='s').finalize().extrude(-69).union(w0.sketch().push([(5.5,0)]).rect(5,20).push([(7,3.5)]).rect(2,3,mode='s').finalize().extrude(9))