import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
r=w0.sketch().segment((-66,-99),(-60,-100)).segment((-59,-86)).close().assemble().finalize().extrude(111).union(w0.sketch().push([(29,92)]).rect(74,16).push([(42.5,94)]).rect(11,6,mode='s').finalize().extrude(159))