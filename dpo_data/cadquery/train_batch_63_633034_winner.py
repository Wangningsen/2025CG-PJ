import cadquery as cq
w0=cq.Workplane('YZ',origin=(56,0,0))
r=w0.sketch().push([(-74,0)]).rect(52,198).push([(73,0)]).rect(54,198).finalize().extrude(-112)