1 stdcall -private DllCanUnloadNow()
2 stdcall -private DllGetClassObject(ptr ptr ptr)
3 stdcall -private DllRegisterServer()
4 stdcall -private DllUnregisterServer()
10 stdcall AtlAdvise(ptr ptr ptr ptr)
11 stdcall AtlUnadvise(ptr ptr long)
12 stdcall AtlFreeMarshalStream(ptr)
13 stdcall AtlMarshalPtrInProc(ptr ptr ptr)
14 stdcall AtlUnmarshalPtr(ptr ptr ptr)
15 stdcall AtlModuleGetClassObject(ptr ptr ptr ptr)
16 stdcall AtlModuleInit(ptr ptr long)
17 stdcall AtlModuleRegisterClassObjects(ptr long long)
18 stdcall AtlModuleRegisterServer(ptr long ptr)
19 stdcall AtlModuleRegisterTypeLib(ptr wstr)
20 stdcall AtlModuleRevokeClassObjects(ptr)
21 stdcall AtlModuleTerm(ptr)
22 stdcall AtlModuleUnregisterServer(ptr ptr)
23 stdcall AtlModuleUpdateRegistryFromResourceD(ptr wstr long ptr ptr)
24 stdcall AtlWaitWithMessageLoop(long)
25 stub AtlSetErrorInfo
26 stdcall AtlCreateTargetDC(long ptr)
27 stdcall AtlHiMetricToPixel(ptr ptr)
28 stdcall AtlPixelToHiMetric(ptr ptr)
29 stub AtlDevModeW2A
30 stdcall AtlComPtrAssign(ptr ptr)
31 stdcall AtlComQIPtrAssign(ptr ptr ptr)
32 stdcall AtlInternalQueryInterface(ptr ptr ptr ptr)
34 stdcall AtlGetVersion(ptr)
35 stdcall AtlAxDialogBoxW(long wstr long ptr long)
36 stdcall AtlAxDialogBoxA(long str long ptr long)
37 stdcall AtlAxCreateDialogW(long wstr long ptr long)
38 stdcall AtlAxCreateDialogA(long str long ptr long)
39 stdcall AtlAxCreateControl(ptr ptr ptr ptr)
40 stdcall AtlAxCreateControlEx(ptr ptr ptr ptr ptr ptr ptr)
41 stdcall AtlAxAttachControl(ptr ptr ptr)
42 stdcall AtlAxWinInit()
43 stdcall AtlModuleAddCreateWndData(ptr ptr ptr)
44 stdcall AtlModuleExtractCreateWndData(ptr)
45 stdcall AtlModuleRegisterWndClassInfoW(ptr ptr ptr)
46 stdcall AtlModuleRegisterWndClassInfoA(ptr ptr ptr)
47 stdcall AtlAxGetControl(long ptr)
48 stdcall AtlAxGetHost(long ptr)
49 stdcall AtlRegisterClassCategoriesHelper(ptr ptr long)
50 stdcall AtlIPersistStreamInit_Load(ptr ptr ptr ptr)
51 stdcall AtlIPersistStreamInit_Save(ptr long ptr ptr ptr)
52 stdcall AtlIPersistPropertyBag_Load(ptr ptr ptr ptr ptr)
53 stdcall AtlIPersistPropertyBag_Save(ptr long long ptr ptr ptr)
54 stdcall AtlGetObjectSourceInterface(ptr ptr ptr ptr ptr)
55 stub AtlModuleUnRegisterTypeLib
56 stdcall AtlModuleLoadTypeLib(ptr wstr ptr ptr)
57 stdcall AtlModuleUnregisterServerEx(ptr long ptr)
58 stdcall AtlModuleAddTermFunc(ptr ptr long)
