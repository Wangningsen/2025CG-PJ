import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().segment((-96,38),(-26,-100)).segment((96,-38)).segment((26,100)).close().assemble().push([(5,69)]).rect(48,18,mode='s').finalize().extrude(-37)