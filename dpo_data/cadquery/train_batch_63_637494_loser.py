import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.sketch().segment((-53,-8),(14,-8)).segment((14,-13)).segment((40,-13)).segment((40,-8)).segment((45,-8)).segment((45,56)).segment((30,56)).segment((30,70)).segment((-25,70)).segment((-25,69)).segment((-53,70)).close().assemble().push([(43.5,-53.5)]).rect(7,93).push([(50,80)]).rect(6,40).finalize().extrude(14)