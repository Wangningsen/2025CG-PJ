import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-66,0))
r=w0.sketch().segment((-96,-52),(-84,-52)).segment((-84,-94)).segment((-31,-94)).arc((-18,-99),(-10,-88)).segment((-25,-52)).segment((96,-52)).segment((96,52)).segment((84,52)).segment((84,94)).segment((31,94)).arc((18,99),(10,94)).segment((-2,94)).segment((25,52)).segment((-96,52)).close().assemble().finalize().extrude(132)