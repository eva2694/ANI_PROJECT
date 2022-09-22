/*********************************** 
 * Constellations_Nai2022_Eng Test *
 ***********************************/


// store info about the experiment session:
let expName = 'Constellations_NAI2022_ENG';  // from the Builder filename that created this script
let expInfo = {'Pseudonym*': '', 'Age': '', 'Gender': ''};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'norm',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(intro0RoutineBegin());
flowScheduler.add(intro0RoutineEachFrame());
flowScheduler.add(intro0RoutineEnd());
flowScheduler.add(intro1RoutineBegin());
flowScheduler.add(intro1RoutineEachFrame());
flowScheduler.add(intro1RoutineEnd());
flowScheduler.add(intro2RoutineBegin());
flowScheduler.add(intro2RoutineEachFrame());
flowScheduler.add(intro2RoutineEnd());
flowScheduler.add(intro3RoutineBegin());
flowScheduler.add(intro3RoutineEachFrame());
flowScheduler.add(intro3RoutineEnd());
flowScheduler.add(practice_introRoutineBegin());
flowScheduler.add(practice_introRoutineEachFrame());
flowScheduler.add(practice_introRoutineEnd());
flowScheduler.add(practice_trialRoutineBegin());
flowScheduler.add(practice_trialRoutineEachFrame());
flowScheduler.add(practice_trialRoutineEnd());
flowScheduler.add(practice_rspRoutineBegin());
flowScheduler.add(practice_rspRoutineEachFrame());
flowScheduler.add(practice_rspRoutineEnd());
flowScheduler.add(exp_introRoutineBegin());
flowScheduler.add(exp_introRoutineEachFrame());
flowScheduler.add(exp_introRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(pauseRoutineBegin());
flowScheduler.add(pauseRoutineEachFrame());
flowScheduler.add(pauseRoutineEnd());
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/gramophone_01b_9.jpg', 'path': 'stimuli/gramophone_01b_9.jpg'},
    {'name': 'stimuli/dolphin_14s_11.jpg', 'path': 'stimuli/dolphin_14s_11.jpg'},
    {'name': 'stimuli/bottle_02n_11.jpg', 'path': 'stimuli/bottle_02n_11.jpg'},
    {'name': 'stimuli/intro4.PNG', 'path': 'stimuli/intro4.PNG'},
    {'name': 'stimuli/margarita_17s_11.jpg', 'path': 'stimuli/margarita_17s_11.jpg'},
    {'name': 'stimuli/bathrobe_02s_11.jpg', 'path': 'stimuli/bathrobe_02s_11.jpg'},
    {'name': 'stimuli/teapot_06s_9.jpg', 'path': 'stimuli/teapot_06s_9.jpg'},
    {'name': 'stimuli/bottle_02n_9.jpg', 'path': 'stimuli/bottle_02n_9.jpg'},
    {'name': 'stimuli/mask_12s_9.jpg', 'path': 'stimuli/mask_12s_9.jpg'},
    {'name': 'stimuli/hammer_07s_11.jpg', 'path': 'stimuli/hammer_07s_11.jpg'},
    {'name': 'stimuli/bag_04s_9.jpg', 'path': 'stimuli/bag_04s_9.jpg'},
    {'name': 'stimuli/hammer_07s_9.jpg', 'path': 'stimuli/hammer_07s_9.jpg'},
    {'name': 'stimuli/racehorse_07s_11.jpg', 'path': 'stimuli/racehorse_07s_11.jpg'},
    {'name': 'stimuli/kangaroo_02s_11.jpg', 'path': 'stimuli/kangaroo_02s_11.jpg'},
    {'name': 'stimuli/beer_05s_11.jpg', 'path': 'stimuli/beer_05s_11.jpg'},
    {'name': 'stimuli/dragonfly_07s_9.jpg', 'path': 'stimuli/dragonfly_07s_9.jpg'},
    {'name': 'stimuli/man_09s_11.jpg', 'path': 'stimuli/man_09s_11.jpg'},
    {'name': 'stimuli/boxing_gloves_06s_9.jpg', 'path': 'stimuli/boxing_gloves_06s_9.jpg'},
    {'name': 'stimuli/seahorse_02s_9.jpg', 'path': 'stimuli/seahorse_02s_9.jpg'},
    {'name': 'stimuli/teddy_bear_06s_11.jpg', 'path': 'stimuli/teddy_bear_06s_11.jpg'},
    {'name': 'stimuli/axe_12n_9.jpg', 'path': 'stimuli/axe_12n_9.jpg'},
    {'name': 'stimuli/bird_18s_11.jpg', 'path': 'stimuli/bird_18s_11.jpg'},
    {'name': 'stimuli/bird_18s_9.jpg', 'path': 'stimuli/bird_18s_9.jpg'},
    {'name': 'stimuli/toilet_paper_02s_9.jpg', 'path': 'stimuli/toilet_paper_02s_9.jpg'},
    {'name': 'stimuli/dragonfly_07s_11.jpg', 'path': 'stimuli/dragonfly_07s_11.jpg'},
    {'name': 'stimuli/teddy_bear_06s_9.jpg', 'path': 'stimuli/teddy_bear_06s_9.jpg'},
    {'name': 'stimuli/hat_07s_9.jpg', 'path': 'stimuli/hat_07s_9.jpg'},
    {'name': 'stimuli/clipper1_07s_9.jpg', 'path': 'stimuli/clipper1_07s_9.jpg'},
    {'name': 'stimuli/magnifying_glass_01b_9.jpg', 'path': 'stimuli/magnifying_glass_01b_9.jpg'},
    {'name': 'stimuli/recliner_10s_11.jpg', 'path': 'stimuli/recliner_10s_11.jpg'},
    {'name': 'stimuli/swan_11s_9.jpg', 'path': 'stimuli/swan_11s_9.jpg'},
    {'name': 'trial_online.csv', 'path': 'trial_online.csv'},
    {'name': 'stimuli/practice_first.jpg', 'path': 'stimuli/practice_first.jpg'},
    {'name': 'stimuli/man_09s_9.jpg', 'path': 'stimuli/man_09s_9.jpg'},
    {'name': 'stimuli/gramophone_01b_11.jpg', 'path': 'stimuli/gramophone_01b_11.jpg'},
    {'name': 'stimuli/intro2.PNG', 'path': 'stimuli/intro2.PNG'},
    {'name': 'stimuli/horse_08s_11.jpg', 'path': 'stimuli/horse_08s_11.jpg'},
    {'name': 'stimuli/glasses_13s_11.jpg', 'path': 'stimuli/glasses_13s_11.jpg'},
    {'name': 'stimuli/margarita_17s_9.jpg', 'path': 'stimuli/margarita_17s_9.jpg'},
    {'name': 'stimuli/recliner_10s_9.jpg', 'path': 'stimuli/recliner_10s_9.jpg'},
    {'name': 'stimuli/mask_12s_11.jpg', 'path': 'stimuli/mask_12s_11.jpg'},
    {'name': 'stimuli/hat_07s_11.jpg', 'path': 'stimuli/hat_07s_11.jpg'},
    {'name': 'stimuli/clipper1_07s_11.jpg', 'path': 'stimuli/clipper1_07s_11.jpg'},
    {'name': 'stimuli/puppy_12s_11.jpg', 'path': 'stimuli/puppy_12s_11.jpg'},
    {'name': 'stimuli/intro3.PNG', 'path': 'stimuli/intro3.PNG'},
    {'name': 'stimuli/seahorse_02s_11.jpg', 'path': 'stimuli/seahorse_02s_11.jpg'},
    {'name': 'stimuli/hairdryer_10s_9.jpg', 'path': 'stimuli/hairdryer_10s_9.jpg'},
    {'name': 'stimuli/headphones_01b_9.jpg', 'path': 'stimuli/headphones_01b_9.jpg'},
    {'name': 'stimuli/solution1.jpg', 'path': 'stimuli/solution1.jpg'},
    {'name': 'stimuli/axe_12n_11.jpg', 'path': 'stimuli/axe_12n_11.jpg'},
    {'name': 'stimuli/gun_01b_11.jpg', 'path': 'stimuli/gun_01b_11.jpg'},
    {'name': 'stimuli/hairdryer_10s_11.jpg', 'path': 'stimuli/hairdryer_10s_11.jpg'},
    {'name': 'stimuli/dolphin_14s_9.jpg', 'path': 'stimuli/dolphin_14s_9.jpg'},
    {'name': 'stimuli/intro0.PNG', 'path': 'stimuli/intro0.PNG'},
    {'name': 'stimuli/glasses_13s_9.jpg', 'path': 'stimuli/glasses_13s_9.jpg'},
    {'name': 'stimuli/gun_01b_9.jpg', 'path': 'stimuli/gun_01b_9.jpg'},
    {'name': 'stimuli/wine_17s_9.jpg', 'path': 'stimuli/wine_17s_9.jpg'},
    {'name': 'stimuli/penguin_12s_11.jpg', 'path': 'stimuli/penguin_12s_11.jpg'},
    {'name': 'stimuli/kangaroo_02s_9.jpg', 'path': 'stimuli/kangaroo_02s_9.jpg'},
    {'name': 'stimuli/stiletto_10s_11.jpg', 'path': 'stimuli/stiletto_10s_11.jpg'},
    {'name': 'stimuli/headphones_01b_11.jpg', 'path': 'stimuli/headphones_01b_11.jpg'},
    {'name': 'stimuli/magnifying_glass_01b_11.jpg', 'path': 'stimuli/magnifying_glass_01b_11.jpg'},
    {'name': 'stimuli/anchor_02s_9.jpg', 'path': 'stimuli/anchor_02s_9.jpg'},
    {'name': 'stimuli/anchor_02s_11.jpg', 'path': 'stimuli/anchor_02s_11.jpg'},
    {'name': 'stimuli/bag_04s_11.jpg', 'path': 'stimuli/bag_04s_11.jpg'},
    {'name': 'stimuli/cello_01s_11.jpg', 'path': 'stimuli/cello_01s_11.jpg'},
    {'name': 'stimuli/coffee_04s_11.jpg', 'path': 'stimuli/coffee_04s_11.jpg'},
    {'name': 'stimuli/swan_11s_11.jpg', 'path': 'stimuli/swan_11s_11.jpg'},
    {'name': 'stimuli/horse_08s_9.jpg', 'path': 'stimuli/horse_08s_9.jpg'},
    {'name': 'stimuli/beer_05s_9.jpg', 'path': 'stimuli/beer_05s_9.jpg'},
    {'name': 'stimuli/puppy_12s_9.jpg', 'path': 'stimuli/puppy_12s_9.jpg'},
    {'name': 'stimuli/penguin_12s_9.jpg', 'path': 'stimuli/penguin_12s_9.jpg'},
    {'name': 'stimuli/boot_02s_11.jpg', 'path': 'stimuli/boot_02s_11.jpg'},
    {'name': 'stimuli/racehorse_07s_9.jpg', 'path': 'stimuli/racehorse_07s_9.jpg'},
    {'name': 'stimuli/intro5.PNG', 'path': 'stimuli/intro5.PNG'},
    {'name': 'stimuli/toilet_paper_02s_11.jpg', 'path': 'stimuli/toilet_paper_02s_11.jpg'},
    {'name': 'stimuli/teapot_06s_11.jpg', 'path': 'stimuli/teapot_06s_11.jpg'},
    {'name': 'stimuli/boot_02s_9.jpg', 'path': 'stimuli/boot_02s_9.jpg'},
    {'name': 'stimuli/cello_01s_9.jpg', 'path': 'stimuli/cello_01s_9.jpg'},
    {'name': 'stimuli/intro1.PNG', 'path': 'stimuli/intro1.PNG'},
    {'name': 'stimuli/coffee_04s_9.jpg', 'path': 'stimuli/coffee_04s_9.jpg'},
    {'name': 'stimuli/stiletto_10s_9.jpg', 'path': 'stimuli/stiletto_10s_9.jpg'},
    {'name': 'stimuli/boxing_gloves_06s_11.jpg', 'path': 'stimuli/boxing_gloves_06s_11.jpg'},
    {'name': 'stimuli/wine_17s_11.jpg', 'path': 'stimuli/wine_17s_11.jpg'},
    {'name': 'stimuli/bathrobe_02s_9.jpg', 'path': 'stimuli/bathrobe_02s_9.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var intro0Clock;
var instruction1_2;
var mouse1_2;
var button1_2;
var button_txt1_2;
var intro1Clock;
var instruction1;
var mouse1;
var button1;
var button_txt1;
var intro2Clock;
var instruction2;
var mouse2;
var button2;
var button_txt2;
var intro3Clock;
var instruction3;
var mouse3;
var button3;
var button_txt3;
var practice_introClock;
var instruction4;
var mouse4;
var button4;
var button_txt4;
var practice_trialClock;
var image_2;
var brush_2;
var getbrush_2;
var brush_2Reset;
var brush_2CurrentShape;
var brush_2BrushPos;
var brush_2Pointer;
var brush_2AtStartPoint;
var brush_2Shapes;
var mouse_track_2;
var H1_textbox_2;
var juhis_txt_2;
var button_clear_2;
var objekt_txt_2;
var mouse_2;
var button_next_2;
var mouse_end_2;
var clear_txt_2;
var button_hint_2;
var vihje_txt_2;
var button_yes_2;
var leidsin_txt_2;
var RSP_ahhaa_2;
var ahhaa_txt_2;
var RSP_sudden_2;
var sudden_txt_2;
var RSP_pleasant_2;
var pleasant_txt_2;
var next_txt_2;
var practice_rspClock;
var practice_object;
var practice_outline;
var text_2;
var mouse5;
var button5;
var button_txt5;
var exp_introClock;
var instruction4_2;
var mouse4_2;
var button4_2;
var button_txt4_2;
var trialClock;
var image;
var stim;
var Version;
var vrs;
var mouse_track;
var brush;
var getbrush;
var brushReset;
var brushCurrentShape;
var brushBrushPos;
var brushPointer;
var brushAtStartPoint;
var brushShapes;
var H1_textbox;
var juhis_txt;
var button_clear;
var objekt_txt;
var mouse;
var button_next;
var mouse_end;
var clear_txt;
var button_hint;
var vihje_txt;
var button_yes;
var leidsin_txt;
var RSP_ahhaa;
var ahhaa_txt;
var RSP_sudden;
var sudden_txt;
var RSP_pleasant;
var pleasant_txt;
var next_txt;
var pauseClock;
var text;
var endClock;
var end_txt;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro0"
  intro0Clock = new util.Clock();
  instruction1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction1_2', units : undefined, 
    image : 'stimuli/intro0.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse1_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse1_2.mouseClock = new util.Clock();
  button1_2 = new visual.Rect ({
    win: psychoJS.window, name: 'button1_2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.65)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  button_txt1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt1_2',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.65)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "intro1"
  intro1Clock = new util.Clock();
  instruction1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction1', units : undefined, 
    image : 'stimuli/intro1.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse1 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse1.mouseClock = new util.Clock();
  button1 = new visual.Rect ({
    win: psychoJS.window, name: 'button1', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.65)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  button_txt1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt1',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.65)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "intro2"
  intro2Clock = new util.Clock();
  instruction2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction2', units : undefined, 
    image : 'stimuli/intro2.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse2.mouseClock = new util.Clock();
  button2 = new visual.Rect ({
    win: psychoJS.window, name: 'button2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.65)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  button_txt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt2',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.65)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "intro3"
  intro3Clock = new util.Clock();
  instruction3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction3', units : undefined, 
    image : 'stimuli/intro3.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse3.mouseClock = new util.Clock();
  button3 = new visual.Rect ({
    win: psychoJS.window, name: 'button3', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.65)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  button_txt3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt3',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.65)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "practice_intro"
  practice_introClock = new util.Clock();
  instruction4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction4', units : undefined, 
    image : 'stimuli/intro4.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse4 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse4.mouseClock = new util.Clock();
  button4 = new visual.Rect ({
    win: psychoJS.window, name: 'button4', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.65)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  button_txt4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt4',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.65)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "practice_trial"
  practice_trialClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.4), 0.0], size : [0.65, 0.65],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  brush_2 = {};
  getbrush_2 = function() {
    return ( new visual.ShapeStim({
      win: psychoJS.window,
      vertices: [[0, 0]],
      lineWidth: 3.0,
      lineColor: new util.Color([1, 1, 1]),
      opacity: null,
      closeShape: false,
      autoLog: false
      }))
  }
  
  brush_2Reset = brush_2.reset = function() {
    if (brush_2Shapes.length > 0) {
      for (let shape of brush_2Shapes) {
        shape.setAutoDraw(false);
      }
    }
    brush_2AtStartPoint = false;
    brush_2Shapes = [];
    brush_2CurrentShape = -1;
  }
  
  brush_2CurrentShape = -1;
  brush_2BrushPos = [];
  brush_2Pointer = new core.Mouse({win: psychoJS.window});
  brush_2AtStartPoint = false;
  brush_2Shapes = [];
  mouse_track_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_track_2.mouseClock = new util.Clock();
  H1_textbox_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'H1_textbox_2',
    text: '',
    font: 'Open Sans',
    pos: [0.15, 0.5], letterHeight: 0.05,
    size: [0.65, 0.4],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'grey',
    bold: false, italic: false,
    opacity: undefined,
    padding: undefined,
    editable: true,
    multiline: true,
    anchor: 'top-left',
    depth: -3.0 
  });
  
  juhis_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'juhis_txt_2',
    text: 'Trace the contours to find an object!',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.75], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  button_clear_2 = new visual.Rect ({
    win: psychoJS.window, name: 'button_clear_2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [(- 0.2), (- 0.75)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  objekt_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'objekt_txt_2',
    text: 'What did you find in the image?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.4, 0.55], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  button_next_2 = new visual.Rect ({
    win: psychoJS.window, name: 'button_next_2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.7, (- 0.75)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  mouse_end_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_end_2.mouseClock = new util.Clock();
  clear_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'clear_txt_2',
    text: 'Erase',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), (- 0.75)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -11.0 
  });
  
  button_hint_2 = new visual.Rect ({
    win: psychoJS.window, name: 'button_hint_2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.6, 0.6],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('red'),
    opacity: undefined, depth: -12, interpolate: true,
  });
  
  vihje_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'vihje_txt_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, 0.6], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -13.0 
  });
  
  button_yes_2 = new visual.Rect ({
    win: psychoJS.window, name: 'button_yes_2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.3, 0.6],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('green'),
    opacity: undefined, depth: -14, interpolate: true,
  });
  
  leidsin_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'leidsin_txt_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.3, 0.6], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -15.0 
  });
  
  RSP_ahhaa_2 = new visual.Slider({
    win: psychoJS.window, name: 'RSP_ahhaa_2',
    size: [0.5, 0.06], pos: [0.5, (- 0.05)], units: 'norm',
    labels: ["Very uncertain", "Very certain"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -16, 
    flip: false,
  });
  
  ahhaa_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ahhaa_txt_2',
    text: 'How certain are you that your answer is correct?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.51, 0.05], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -17.0 
  });
  
  RSP_sudden_2 = new visual.Slider({
    win: psychoJS.window, name: 'RSP_sudden_2',
    size: [0.5, 0.06], pos: [0.5, (- 0.3)], units: 'norm',
    labels: ["Very gradually", "Very suddenly"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -18, 
    flip: false,
  });
  
  sudden_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'sudden_txt_2',
    text: 'How suddenly did the final answer arrive?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.42, (- 0.2)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -19.0 
  });
  
  RSP_pleasant_2 = new visual.Slider({
    win: psychoJS.window, name: 'RSP_pleasant_2',
    size: [0.5, 0.06], pos: [0.5, (- 0.55)], units: 'norm',
    labels: ["Very easy", "Very difficult"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -20, 
    flip: false,
  });
  
  pleasant_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'pleasant_txt_2',
    text: 'How difficult was it to find a solution?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.42, (- 0.45)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -21.0 
  });
  
  next_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_txt_2',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.7, (- 0.75)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -22.0 
  });
  
  // Initialize components for Routine "practice_rsp"
  practice_rspClock = new util.Clock();
  practice_object = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practice_object', units : 'height', 
    image : 'stimuli/practice_first.jpg', mask : undefined,
    ori : 0.0, pos : [0.0, 0.0], size : [0.65, 0.65],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  practice_outline = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practice_outline', units : 'height', 
    image : 'stimuli/solution1.jpg', mask : undefined,
    ori : 0.0, pos : [0.0, 0.0], size : [0.65, 0.65],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Answer: CAR',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.7], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouse5 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse5.mouseClock = new util.Clock();
  button5 = new visual.Rect ({
    win: psychoJS.window, name: 'button5', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.6)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  button_txt5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt5',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.6)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "exp_intro"
  exp_introClock = new util.Clock();
  instruction4_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instruction4_2', units : undefined, 
    image : 'stimuli/intro5.PNG', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  mouse4_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse4_2.mouseClock = new util.Clock();
  button4_2 = new visual.Rect ({
    win: psychoJS.window, name: 'button4_2', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.5, (- 0.65)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  button_txt4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'button_txt4_2',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.65)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.4), 0.0], size : [0.65, 0.65],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  stim = 0;
  Version = 0;
  vrs = util.randint(1, 3).toString();
  console.log(vrs);
  
  mouse_track = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_track.mouseClock = new util.Clock();
  brush = {};
  getbrush = function() {
    return ( new visual.ShapeStim({
      win: psychoJS.window,
      vertices: [[0, 0]],
      lineWidth: 3.0,
      lineColor: new util.Color([1, 1, 1]),
      opacity: null,
      closeShape: false,
      autoLog: false
      }))
  }
  
  brushReset = brush.reset = function() {
    if (brushShapes.length > 0) {
      for (let shape of brushShapes) {
        shape.setAutoDraw(false);
      }
    }
    brushAtStartPoint = false;
    brushShapes = [];
    brushCurrentShape = -1;
  }
  
  brushCurrentShape = -1;
  brushBrushPos = [];
  brushPointer = new core.Mouse({win: psychoJS.window});
  brushAtStartPoint = false;
  brushShapes = [];
  H1_textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'H1_textbox',
    text: '',
    font: 'Open Sans',
    pos: [0.15, 0.5], letterHeight: 0.05,
    size: [0.65, 0.4],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'grey',
    bold: false, italic: false,
    opacity: undefined,
    padding: undefined,
    editable: true,
    multiline: true,
    anchor: 'top-left',
    depth: -4.0 
  });
  
  juhis_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'juhis_txt',
    text: 'Trace the contours to find an object!',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.75], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  button_clear = new visual.Rect ({
    win: psychoJS.window, name: 'button_clear', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [(- 0.2), (- 0.75)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  objekt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'objekt_txt',
    text: 'What did you find in the image?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.4, 0.55], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  button_next = new visual.Rect ({
    win: psychoJS.window, name: 'button_next', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.7, (- 0.75)],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -10, interpolate: true,
  });
  
  mouse_end = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_end.mouseClock = new util.Clock();
  clear_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'clear_txt',
    text: 'Erase',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), (- 0.75)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -12.0 
  });
  
  button_hint = new visual.Rect ({
    win: psychoJS.window, name: 'button_hint', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.6, 0.6],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('red'),
    opacity: undefined, depth: -13, interpolate: true,
  });
  
  vihje_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'vihje_txt',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, 0.6], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -14.0 
  });
  
  button_yes = new visual.Rect ({
    win: psychoJS.window, name: 'button_yes', 
    width: [0.2, 0.1][0], height: [0.2, 0.1][1],
    ori: 0.0, pos: [0.3, 0.6],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('green'),
    opacity: undefined, depth: -15, interpolate: true,
  });
  
  leidsin_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'leidsin_txt',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.3, 0.6], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -16.0 
  });
  
  RSP_ahhaa = new visual.Slider({
    win: psychoJS.window, name: 'RSP_ahhaa',
    size: [0.5, 0.06], pos: [0.5, (- 0.05)], units: 'norm',
    labels: ["Very uncertain", "Very certain"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -17, 
    flip: false,
  });
  
  ahhaa_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'ahhaa_txt',
    text: 'How certain are you that your answer is correct?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.51, 0.05], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -18.0 
  });
  
  RSP_sudden = new visual.Slider({
    win: psychoJS.window, name: 'RSP_sudden',
    size: [0.5, 0.06], pos: [0.5, (- 0.3)], units: 'norm',
    labels: ["Very gradually", "Very suddenly"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -19, 
    flip: false,
  });
  
  sudden_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'sudden_txt',
    text: 'How suddenly did the final answer arrive?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.42, (- 0.2)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -20.0 
  });
  
  RSP_pleasant = new visual.Slider({
    win: psychoJS.window, name: 'RSP_pleasant',
    size: [0.5, 0.06], pos: [0.5, (- 0.55)], units: 'norm',
    labels: ["Very easy", "Very difficult"], ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    fontFamily: 'Open Sans', bold: true, italic: false, depth: -21, 
    flip: false,
  });
  
  pleasant_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pleasant_txt',
    text: 'How difficult was it to find a solution?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.42, (- 0.45)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -22.0 
  });
  
  next_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_txt',
    text: 'Next',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.7, (- 0.75)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -23.0 
  });
  
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  end_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_txt',
    text: 'The end. Thank you!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var gotValidClick;
var intro0Components;
function intro0RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'intro0'-------
    t = 0;
    intro0Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse1_2
    mouse1_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    intro0Components = [];
    intro0Components.push(instruction1_2);
    intro0Components.push(mouse1_2);
    intro0Components.push(button1_2);
    intro0Components.push(button_txt1_2);
    
    intro0Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function intro0RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'intro0'-------
    // get current time
    t = intro0Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction1_2* updates
    if (t >= 0.0 && instruction1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction1_2.tStart = t;  // (not accounting for frame time here)
      instruction1_2.frameNStart = frameN;  // exact frame index
      
      instruction1_2.setAutoDraw(true);
    }

    // *mouse1_2* updates
    if (t >= 0.0 && mouse1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse1_2.tStart = t;  // (not accounting for frame time here)
      mouse1_2.frameNStart = frameN;  // exact frame index
      
      mouse1_2.status = PsychoJS.Status.STARTED;
      mouse1_2.mouseClock.reset();
      prevButtonState = mouse1_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse1_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse1_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button1_2,]) {
            if (obj.contains(mouse1_2)) {
              gotValidClick = true;
              mouse1_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button1_2* updates
    if (t >= 0.0 && button1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button1_2.tStart = t;  // (not accounting for frame time here)
      button1_2.frameNStart = frameN;  // exact frame index
      
      button1_2.setAutoDraw(true);
    }

    
    // *button_txt1_2* updates
    if (t >= 0.0 && button_txt1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt1_2.tStart = t;  // (not accounting for frame time here)
      button_txt1_2.frameNStart = frameN;  // exact frame index
      
      button_txt1_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    intro0Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intro0RoutineEnd() {
  return async function () {
    //------Ending Routine 'intro0'-------
    intro0Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "intro0" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var intro1Components;
function intro1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'intro1'-------
    t = 0;
    intro1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse1
    mouse1.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    intro1Components = [];
    intro1Components.push(instruction1);
    intro1Components.push(mouse1);
    intro1Components.push(button1);
    intro1Components.push(button_txt1);
    
    intro1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function intro1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'intro1'-------
    // get current time
    t = intro1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction1* updates
    if (t >= 0.0 && instruction1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction1.tStart = t;  // (not accounting for frame time here)
      instruction1.frameNStart = frameN;  // exact frame index
      
      instruction1.setAutoDraw(true);
    }

    // *mouse1* updates
    if (t >= 2.0 && mouse1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse1.tStart = t;  // (not accounting for frame time here)
      mouse1.frameNStart = frameN;  // exact frame index
      
      mouse1.status = PsychoJS.Status.STARTED;
      mouse1.mouseClock.reset();
      prevButtonState = mouse1.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse1.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse1.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button1,]) {
            if (obj.contains(mouse1)) {
              gotValidClick = true;
              mouse1.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button1* updates
    if (t >= 2.0 && button1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button1.tStart = t;  // (not accounting for frame time here)
      button1.frameNStart = frameN;  // exact frame index
      
      button1.setAutoDraw(true);
    }

    
    // *button_txt1* updates
    if (t >= 2.0 && button_txt1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt1.tStart = t;  // (not accounting for frame time here)
      button_txt1.frameNStart = frameN;  // exact frame index
      
      button_txt1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    intro1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intro1RoutineEnd() {
  return async function () {
    //------Ending Routine 'intro1'-------
    intro1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "intro1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var intro2Components;
function intro2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'intro2'-------
    t = 0;
    intro2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse2
    mouse2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    intro2Components = [];
    intro2Components.push(instruction2);
    intro2Components.push(mouse2);
    intro2Components.push(button2);
    intro2Components.push(button_txt2);
    
    intro2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function intro2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'intro2'-------
    // get current time
    t = intro2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction2* updates
    if (t >= 0.0 && instruction2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction2.tStart = t;  // (not accounting for frame time here)
      instruction2.frameNStart = frameN;  // exact frame index
      
      instruction2.setAutoDraw(true);
    }

    // *mouse2* updates
    if (t >= 2.0 && mouse2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse2.tStart = t;  // (not accounting for frame time here)
      mouse2.frameNStart = frameN;  // exact frame index
      
      mouse2.status = PsychoJS.Status.STARTED;
      mouse2.mouseClock.reset();
      prevButtonState = mouse2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button2,]) {
            if (obj.contains(mouse2)) {
              gotValidClick = true;
              mouse2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button2* updates
    if (t >= 2.0 && button2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button2.tStart = t;  // (not accounting for frame time here)
      button2.frameNStart = frameN;  // exact frame index
      
      button2.setAutoDraw(true);
    }

    
    // *button_txt2* updates
    if (t >= 2.0 && button_txt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt2.tStart = t;  // (not accounting for frame time here)
      button_txt2.frameNStart = frameN;  // exact frame index
      
      button_txt2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    intro2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intro2RoutineEnd() {
  return async function () {
    //------Ending Routine 'intro2'-------
    intro2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var intro3Components;
function intro3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'intro3'-------
    t = 0;
    intro3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse3
    mouse3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    intro3Components = [];
    intro3Components.push(instruction3);
    intro3Components.push(mouse3);
    intro3Components.push(button3);
    intro3Components.push(button_txt3);
    
    intro3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function intro3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'intro3'-------
    // get current time
    t = intro3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction3* updates
    if (t >= 0.0 && instruction3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction3.tStart = t;  // (not accounting for frame time here)
      instruction3.frameNStart = frameN;  // exact frame index
      
      instruction3.setAutoDraw(true);
    }

    // *mouse3* updates
    if (t >= 2.0 && mouse3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse3.tStart = t;  // (not accounting for frame time here)
      mouse3.frameNStart = frameN;  // exact frame index
      
      mouse3.status = PsychoJS.Status.STARTED;
      mouse3.mouseClock.reset();
      prevButtonState = mouse3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button3,]) {
            if (obj.contains(mouse3)) {
              gotValidClick = true;
              mouse3.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button3* updates
    if (t >= 2.0 && button3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button3.tStart = t;  // (not accounting for frame time here)
      button3.frameNStart = frameN;  // exact frame index
      
      button3.setAutoDraw(true);
    }

    
    // *button_txt3* updates
    if (t >= 2.0 && button_txt3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt3.tStart = t;  // (not accounting for frame time here)
      button_txt3.frameNStart = frameN;  // exact frame index
      
      button_txt3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    intro3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intro3RoutineEnd() {
  return async function () {
    //------Ending Routine 'intro3'-------
    intro3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "intro3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice_introComponents;
function practice_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practice_intro'-------
    t = 0;
    practice_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse4
    mouse4.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    practice_introComponents = [];
    practice_introComponents.push(instruction4);
    practice_introComponents.push(mouse4);
    practice_introComponents.push(button4);
    practice_introComponents.push(button_txt4);
    
    practice_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_introRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practice_intro'-------
    // get current time
    t = practice_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction4* updates
    if (t >= 0.0 && instruction4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction4.tStart = t;  // (not accounting for frame time here)
      instruction4.frameNStart = frameN;  // exact frame index
      
      instruction4.setAutoDraw(true);
    }

    // *mouse4* updates
    if (t >= 2.0 && mouse4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse4.tStart = t;  // (not accounting for frame time here)
      mouse4.frameNStart = frameN;  // exact frame index
      
      mouse4.status = PsychoJS.Status.STARTED;
      mouse4.mouseClock.reset();
      prevButtonState = mouse4.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button4,]) {
            if (obj.contains(mouse4)) {
              gotValidClick = true;
              mouse4.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button4* updates
    if (t >= 2.0 && button4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button4.tStart = t;  // (not accounting for frame time here)
      button4.frameNStart = frameN;  // exact frame index
      
      button4.setAutoDraw(true);
    }

    
    // *button_txt4* updates
    if (t >= 2.0 && button_txt4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt4.tStart = t;  // (not accounting for frame time here)
      button_txt4.frameNStart = frameN;  // exact frame index
      
      button_txt4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_introRoutineEnd() {
  return async function () {
    //------Ending Routine 'practice_intro'-------
    practice_introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "practice_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var RSP;
var Valmis;
var Yes;
var Vihje;
var Nupp;
var frames;
var mouseIsDown;
var mouseIsDown1;
var mouseIsDown2;
var oldMouseIsDown;
var practice_trialComponents;
function practice_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practice_trial'-------
    t = 0;
    practice_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image_2.setImage('stimuli/practice_first.jpg');
    brush_2Reset();
    // setup some python lists for storing info about the mouse_track_2
    // current position of the mouse:
    mouse_track_2.x = [];
    mouse_track_2.y = [];
    mouse_track_2.leftButton = [];
    mouse_track_2.midButton = [];
    mouse_track_2.rightButton = [];
    mouse_track_2.time = [];
    gotValidClick = false; // until a click is received
    H1_textbox_2.setText('');
    H1_textbox_2.setText('');
    RSP = 0;
    Valmis = 0;
    Yes = 0;
    Vihje = 0;
    Nupp = 0;
    frames = 0;
    mouseIsDown = false;
    mouseIsDown1 = false;
    mouseIsDown2 = false;
    oldMouseIsDown = false;
    
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // setup some python lists for storing info about the mouse_end_2
    mouse_end_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    vihje_txt_2.setText('None');
    leidsin_txt_2.setText('Found it!');
    RSP_ahhaa_2.reset()
    RSP_sudden_2.reset()
    RSP_pleasant_2.reset()
    // keep track of which components have finished
    practice_trialComponents = [];
    practice_trialComponents.push(image_2);
    practice_trialComponents.push(brush_2);
    practice_trialComponents.push(mouse_track_2);
    practice_trialComponents.push(H1_textbox_2);
    practice_trialComponents.push(juhis_txt_2);
    practice_trialComponents.push(button_clear_2);
    practice_trialComponents.push(objekt_txt_2);
    practice_trialComponents.push(mouse_2);
    practice_trialComponents.push(button_next_2);
    practice_trialComponents.push(mouse_end_2);
    practice_trialComponents.push(clear_txt_2);
    practice_trialComponents.push(button_hint_2);
    practice_trialComponents.push(vihje_txt_2);
    practice_trialComponents.push(button_yes_2);
    practice_trialComponents.push(leidsin_txt_2);
    practice_trialComponents.push(RSP_ahhaa_2);
    practice_trialComponents.push(ahhaa_txt_2);
    practice_trialComponents.push(RSP_sudden_2);
    practice_trialComponents.push(sudden_txt_2);
    practice_trialComponents.push(RSP_pleasant_2);
    practice_trialComponents.push(pleasant_txt_2);
    practice_trialComponents.push(next_txt_2);
    
    practice_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var _mouseXYs;
function practice_trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practice_trial'-------
    // get current time
    t = practice_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    if (brush_2Pointer.getPressed()[0] === 1 && brush_2AtStartPoint != true) {
      brush_2AtStartPoint = true;
      brush_2BrushPos = [];
      brush_2Shapes.push(getbrush_2());
      brush_2CurrentShape += 1;
      brush_2Shapes[brush_2CurrentShape].setAutoDraw(true);
    }
    if (brush_2Pointer.getPressed()[0] === 1) {
      brush_2BrushPos.push(brush_2Pointer.getPos());
      brush_2Shapes[brush_2CurrentShape].setVertices(brush_2BrushPos);
    } else {
      brush_2AtStartPoint = false;
    }
    // *mouse_track_2* updates
    if (t >= 0.0 && mouse_track_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_track_2.tStart = t;  // (not accounting for frame time here)
      mouse_track_2.frameNStart = frameN;  // exact frame index
      
      mouse_track_2.status = PsychoJS.Status.STARTED;
      mouse_track_2.mouseClock.reset();
      prevButtonState = mouse_track_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_track_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_track_2.getPressed();
      _mouseXYs = mouse_track_2.getPos();
      mouse_track_2.x.push(_mouseXYs[0]);
      mouse_track_2.y.push(_mouseXYs[1]);
      mouse_track_2.leftButton.push(_mouseButtons[0]);
      mouse_track_2.midButton.push(_mouseButtons[1]);
      mouse_track_2.rightButton.push(_mouseButtons[2]);
      mouse_track_2.time.push(mouse_track_2.mouseClock.getTime());
    }
    
    // *H1_textbox_2* updates
    if ((Yes == 1) && H1_textbox_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      H1_textbox_2.tStart = t;  // (not accounting for frame time here)
      H1_textbox_2.frameNStart = frameN;  // exact frame index
      
      H1_textbox_2.setAutoDraw(true);
    }

    if ((button_yes_2.contains(mouse_2) && mouse_2.getPressed()[0])) {
        Yes = 1;
        Nupp = 1;
    }
    if ((button_hint_2.contains(mouse_2) && mouse_2.getPressed()[0])) {
        Vihje = 1;
        Nupp = 1;
    }
    if ((Yes == 1)) {
        if (((((RSP_ahhaa_2.getRating() != null) && (H1_textbox_2.text != "")) && (RSP_sudden_2.getRating() != null)) && (RSP_pleasant_2.getRating() != null))) {
            Valmis = 1;
        }
    } else {
        if ((Vihje == 1)) {
            //if ((((RSP_ahhaa_2.getRating() != null) && (RSP_sudden_2.getRating() != null)) && (RSP_pleasant_2.getRating() != null))) {
            Valmis = 1;
        }
    }
    
    if ((button_next_2.contains(mouse_end_2) && (mouse_end_2.getPressed()[0] == 1))) {
        mouseIsDown1 = true;
        if ((mouseIsDown1 && (! oldMouseIsDown))) {
            oldMouseIsDown = true;
        }
    } else {
        mouseIsDown1 = false;
    }
    if ((button_clear_2.contains(mouse_2) && (mouse_2.getPressed()[0] == 1))) {
        mouseIsDown = true;
        if ((mouseIsDown && (! oldMouseIsDown))) {
            brush_2.reset();
        }
    }
    if ((mouseIsDown2 == true)) {
        frames += 1;
        if ((frames < 10)) {
            oldMouseIsDown = true;
        } else {
            mouseIsDown2 = false;
            oldMouseIsDown = false;
            frames = 0;
        }
    }
    if ((mouseIsDown1 == true)) {
        frames += 1;
        if ((frames < 10)) {
            oldMouseIsDown = true;
        } else {
            mouseIsDown1 = false;
            oldMouseIsDown = false;
            frames = 0;
        }
    }
    if ((mouseIsDown == true)) {
        frames += 1;
        if ((frames < 10)) {
            oldMouseIsDown = true;
        } else {
            mouseIsDown = false;
            oldMouseIsDown = false;
            frames = 0;
        }
    }
    
    
    // *juhis_txt_2* updates
    if (t >= 0.0 && juhis_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      juhis_txt_2.tStart = t;  // (not accounting for frame time here)
      juhis_txt_2.frameNStart = frameN;  // exact frame index
      
      juhis_txt_2.setAutoDraw(true);
    }

    
    // *button_clear_2* updates
    if (t >= 0.0 && button_clear_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_clear_2.tStart = t;  // (not accounting for frame time here)
      button_clear_2.frameNStart = frameN;  // exact frame index
      
      button_clear_2.setAutoDraw(true);
    }

    
    // *objekt_txt_2* updates
    if ((Yes == 1) && objekt_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      objekt_txt_2.tStart = t;  // (not accounting for frame time here)
      objekt_txt_2.frameNStart = frameN;  // exact frame index
      
      objekt_txt_2.setAutoDraw(true);
    }

    
    // *button_next_2* updates
    if ((Valmis == 1) && button_next_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_next_2.tStart = t;  // (not accounting for frame time here)
      button_next_2.frameNStart = frameN;  // exact frame index
      
      button_next_2.setAutoDraw(true);
    }

    // *mouse_end_2* updates
    if ((Valmis==1) && mouse_end_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_end_2.tStart = t;  // (not accounting for frame time here)
      mouse_end_2.frameNStart = frameN;  // exact frame index
      
      mouse_end_2.status = PsychoJS.Status.STARTED;
      mouse_end_2.mouseClock.reset();
      prevButtonState = mouse_end_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_end_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_end_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button_next_2]) {
            if (obj.contains(mouse_end_2)) {
              gotValidClick = true;
              mouse_end_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *clear_txt_2* updates
    if (t >= 0.0 && clear_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      clear_txt_2.tStart = t;  // (not accounting for frame time here)
      clear_txt_2.frameNStart = frameN;  // exact frame index
      
      clear_txt_2.setAutoDraw(true);
    }

    
    // *button_hint_2* updates
    if (t >= 5.0 && button_hint_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_hint_2.tStart = t;  // (not accounting for frame time here)
      button_hint_2.frameNStart = frameN;  // exact frame index
      
      button_hint_2.setAutoDraw(true);
    }

    if (button_hint_2.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      button_hint_2.setAutoDraw(false);
    }
    
    // *vihje_txt_2* updates
    if (t >= 5.0 && vihje_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vihje_txt_2.tStart = t;  // (not accounting for frame time here)
      vihje_txt_2.frameNStart = frameN;  // exact frame index
      
      vihje_txt_2.setAutoDraw(true);
    }

    if (vihje_txt_2.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      vihje_txt_2.setAutoDraw(false);
    }
    
    // *button_yes_2* updates
    if (t >= 0.0 && button_yes_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_yes_2.tStart = t;  // (not accounting for frame time here)
      button_yes_2.frameNStart = frameN;  // exact frame index
      
      button_yes_2.setAutoDraw(true);
    }

    if (button_yes_2.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      button_yes_2.setAutoDraw(false);
    }
    
    // *leidsin_txt_2* updates
    if (t >= 0.0 && leidsin_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leidsin_txt_2.tStart = t;  // (not accounting for frame time here)
      leidsin_txt_2.frameNStart = frameN;  // exact frame index
      
      leidsin_txt_2.setAutoDraw(true);
    }

    if (leidsin_txt_2.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      leidsin_txt_2.setAutoDraw(false);
    }
    
    // *RSP_ahhaa_2* updates
    if ((Yes == 1) && RSP_ahhaa_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSP_ahhaa_2.tStart = t;  // (not accounting for frame time here)
      RSP_ahhaa_2.frameNStart = frameN;  // exact frame index
      
      RSP_ahhaa_2.setAutoDraw(true);
    }

    
    // *ahhaa_txt_2* updates
    if ((Yes == 1) && ahhaa_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ahhaa_txt_2.tStart = t;  // (not accounting for frame time here)
      ahhaa_txt_2.frameNStart = frameN;  // exact frame index
      
      ahhaa_txt_2.setAutoDraw(true);
    }

    
    // *RSP_sudden_2* updates
    if ((Yes == 1) && RSP_sudden_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSP_sudden_2.tStart = t;  // (not accounting for frame time here)
      RSP_sudden_2.frameNStart = frameN;  // exact frame index
      
      RSP_sudden_2.setAutoDraw(true);
    }

    
    // *sudden_txt_2* updates
    if ((Yes == 1) && sudden_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sudden_txt_2.tStart = t;  // (not accounting for frame time here)
      sudden_txt_2.frameNStart = frameN;  // exact frame index
      
      sudden_txt_2.setAutoDraw(true);
    }

    
    // *RSP_pleasant_2* updates
    if ((Yes == 1) && RSP_pleasant_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSP_pleasant_2.tStart = t;  // (not accounting for frame time here)
      RSP_pleasant_2.frameNStart = frameN;  // exact frame index
      
      RSP_pleasant_2.setAutoDraw(true);
    }

    
    // *pleasant_txt_2* updates
    if ((Yes == 1) && pleasant_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pleasant_txt_2.tStart = t;  // (not accounting for frame time here)
      pleasant_txt_2.frameNStart = frameN;  // exact frame index
      
      pleasant_txt_2.setAutoDraw(true);
    }

    
    // *next_txt_2* updates
    if ((Valmis == 1) && next_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_txt_2.tStart = t;  // (not accounting for frame time here)
      next_txt_2.frameNStart = frameN;  // exact frame index
      
      next_txt_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'practice_trial'-------
    practice_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_track_2.x', mouse_track_2.x);
    psychoJS.experiment.addData('mouse_track_2.y', mouse_track_2.y);
    psychoJS.experiment.addData('mouse_track_2.leftButton', mouse_track_2.leftButton);
    psychoJS.experiment.addData('mouse_track_2.midButton', mouse_track_2.midButton);
    psychoJS.experiment.addData('mouse_track_2.rightButton', mouse_track_2.rightButton);
    psychoJS.experiment.addData('mouse_track_2.time', mouse_track_2.time);
    
    psychoJS.experiment.addData('H1_textbox_2.text',H1_textbox_2.text)
    H1_textbox_2.refresh();
    brush_2.reset();
    
    // store data for psychoJS.experiment (ExperimentHandler)
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('RSP_ahhaa_2.response', RSP_ahhaa_2.getRating());
    psychoJS.experiment.addData('RSP_ahhaa_2.rt', RSP_ahhaa_2.getRT());
    psychoJS.experiment.addData('RSP_ahhaa_2.history', RSP_ahhaa_2.getHistory());
    psychoJS.experiment.addData('RSP_sudden_2.response', RSP_sudden_2.getRating());
    psychoJS.experiment.addData('RSP_sudden_2.rt', RSP_sudden_2.getRT());
    psychoJS.experiment.addData('RSP_sudden_2.history', RSP_sudden_2.getHistory());
    psychoJS.experiment.addData('RSP_pleasant_2.response', RSP_pleasant_2.getRating());
    psychoJS.experiment.addData('RSP_pleasant_2.rt', RSP_pleasant_2.getRT());
    psychoJS.experiment.addData('RSP_pleasant_2.history', RSP_pleasant_2.getHistory());
    // the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice_rspComponents;
function practice_rspRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'practice_rsp'-------
    t = 0;
    practice_rspClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse5
    mouse5.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    practice_rspComponents = [];
    practice_rspComponents.push(practice_object);
    practice_rspComponents.push(practice_outline);
    practice_rspComponents.push(text_2);
    practice_rspComponents.push(mouse5);
    practice_rspComponents.push(button5);
    practice_rspComponents.push(button_txt5);
    
    practice_rspComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practice_rspRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'practice_rsp'-------
    // get current time
    t = practice_rspClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_object* updates
    if (t >= 0.0 && practice_object.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_object.tStart = t;  // (not accounting for frame time here)
      practice_object.frameNStart = frameN;  // exact frame index
      
      practice_object.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_object.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_object.setAutoDraw(false);
    }
    
    // *practice_outline* updates
    if (t >= 2.0 && practice_outline.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_outline.tStart = t;  // (not accounting for frame time here)
      practice_outline.frameNStart = frameN;  // exact frame index
      
      practice_outline.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // *mouse5* updates
    if (t >= 2.0 && mouse5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse5.tStart = t;  // (not accounting for frame time here)
      mouse5.frameNStart = frameN;  // exact frame index
      
      mouse5.status = PsychoJS.Status.STARTED;
      mouse5.mouseClock.reset();
      prevButtonState = mouse5.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse5.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse5.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button5,]) {
            if (obj.contains(mouse5)) {
              gotValidClick = true;
              mouse5.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button5* updates
    if (t >= 2.0 && button5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button5.tStart = t;  // (not accounting for frame time here)
      button5.frameNStart = frameN;  // exact frame index
      
      button5.setAutoDraw(true);
    }

    
    // *button_txt5* updates
    if (t >= 2.0 && button_txt5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt5.tStart = t;  // (not accounting for frame time here)
      button_txt5.frameNStart = frameN;  // exact frame index
      
      button_txt5.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_rspComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_rspRoutineEnd() {
  return async function () {
    //------Ending Routine 'practice_rsp'-------
    practice_rspComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "practice_rsp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var exp_introComponents;
function exp_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'exp_intro'-------
    t = 0;
    exp_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse4_2
    mouse4_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    exp_introComponents = [];
    exp_introComponents.push(instruction4_2);
    exp_introComponents.push(mouse4_2);
    exp_introComponents.push(button4_2);
    exp_introComponents.push(button_txt4_2);
    
    exp_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function exp_introRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'exp_intro'-------
    // get current time
    t = exp_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction4_2* updates
    if (t >= 0.0 && instruction4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction4_2.tStart = t;  // (not accounting for frame time here)
      instruction4_2.frameNStart = frameN;  // exact frame index
      
      instruction4_2.setAutoDraw(true);
    }

    // *mouse4_2* updates
    if (t >= 2.0 && mouse4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse4_2.tStart = t;  // (not accounting for frame time here)
      mouse4_2.frameNStart = frameN;  // exact frame index
      
      mouse4_2.status = PsychoJS.Status.STARTED;
      mouse4_2.mouseClock.reset();
      prevButtonState = mouse4_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse4_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse4_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button4_2,]) {
            if (obj.contains(mouse4_2)) {
              gotValidClick = true;
              mouse4_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button4_2* updates
    if (t >= 2.0 && button4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button4_2.tStart = t;  // (not accounting for frame time here)
      button4_2.frameNStart = frameN;  // exact frame index
      
      button4_2.setAutoDraw(true);
    }

    
    // *button_txt4_2* updates
    if (t >= 2.0 && button_txt4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_txt4_2.tStart = t;  // (not accounting for frame time here)
      button_txt4_2.frameNStart = frameN;  // exact frame index
      
      button_txt4_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    exp_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exp_introRoutineEnd() {
  return async function () {
    //------Ending Routine 'exp_intro'-------
    exp_introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "exp_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'trial_online.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var buttons;
var times;
var location;
var clear;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image.setImage('stimuli/anchor_02s_9.jpg');
    if ((vrs === "1")) {
        stim = stim1;
    } else {
        if ((vrs === "2")) {
            stim = stim2;
        }
    }
    
    // setup some python lists for storing info about the mouse_track
    // current position of the mouse:
    mouse_track.x = [];
    mouse_track.y = [];
    mouse_track.leftButton = [];
    mouse_track.midButton = [];
    mouse_track.rightButton = [];
    mouse_track.time = [];
    gotValidClick = false; // until a click is received
    brushReset();
    H1_textbox.setText('');
    H1_textbox.setText('');
    RSP = 0;
    Valmis = 0;
    Yes = 0;
    Vihje = 0;
    Nupp = 0;
    frames = 0;
    buttons = 0;
    times = 0;
    location = 0;
    mouseIsDown = false;
    mouseIsDown1 = false;
    mouseIsDown2 = false;
    oldMouseIsDown = false;
    mouse_track.xdraw = [];
    mouse_track.ydraw = [];
    clear = [];
    // setup some python lists for storing info about the mouse
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // setup some python lists for storing info about the mouse_end
    mouse_end.clicked_name = [];
    gotValidClick = false; // until a click is received
    vihje_txt.setText('None');
    leidsin_txt.setText('Found it!');
    RSP_ahhaa.reset()
    RSP_sudden.reset()
    RSP_pleasant.reset()
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(image);
    trialComponents.push(mouse_track);
    trialComponents.push(brush);
    trialComponents.push(H1_textbox);
    trialComponents.push(juhis_txt);
    trialComponents.push(button_clear);
    trialComponents.push(objekt_txt);
    trialComponents.push(mouse);
    trialComponents.push(button_next);
    trialComponents.push(mouse_end);
    trialComponents.push(clear_txt);
    trialComponents.push(button_hint);
    trialComponents.push(vihje_txt);
    trialComponents.push(button_yes);
    trialComponents.push(leidsin_txt);
    trialComponents.push(RSP_ahhaa);
    trialComponents.push(ahhaa_txt);
    trialComponents.push(RSP_sudden);
    trialComponents.push(sudden_txt);
    trialComponents.push(RSP_pleasant);
    trialComponents.push(pleasant_txt);
    trialComponents.push(next_txt);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    // *mouse_track* updates
    if (t >= 0.0 && mouse_track.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_track.tStart = t;  // (not accounting for frame time here)
      mouse_track.frameNStart = frameN;  // exact frame index
      
      mouse_track.status = PsychoJS.Status.STARTED;
      mouse_track.mouseClock.reset();
      prevButtonState = mouse_track.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_track.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_track.getPressed();
      _mouseXYs = mouse_track.getPos();
      mouse_track.x.push(_mouseXYs[0]);
      mouse_track.y.push(_mouseXYs[1]);
      mouse_track.leftButton.push(_mouseButtons[0]);
      mouse_track.midButton.push(_mouseButtons[1]);
      mouse_track.rightButton.push(_mouseButtons[2]);
      mouse_track.time.push(mouse_track.mouseClock.getTime());
    }
    if (brushPointer.getPressed()[0] === 1 && brushAtStartPoint != true) {
      brushAtStartPoint = true;
      brushBrushPos = [];
      brushShapes.push(getbrush());
      brushCurrentShape += 1;
      brushShapes[brushCurrentShape].setAutoDraw(true);
    }
    if (brushPointer.getPressed()[0] === 1) {
      brushBrushPos.push(brushPointer.getPos());
      brushShapes[brushCurrentShape].setVertices(brushBrushPos);
    } else {
      brushAtStartPoint = false;
    }
    
    // *H1_textbox* updates
    if ((Yes == 1) && H1_textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      H1_textbox.tStart = t;  // (not accounting for frame time here)
      H1_textbox.frameNStart = frameN;  // exact frame index
      
      H1_textbox.setAutoDraw(true);
    }

    // Hiire joonistus
    if ((mouse_track.getPressed()[0] == 1)) {
        mouse_track.xdraw.push(mouse_track.getPos()[0]);
        mouse_track.ydraw.push(mouse_track.getPos()[1]);
    }
    
    // Leidsin või vihje nupp tegevus
    if ((button_yes.contains(mouse) && mouse.getPressed()[0])) {
        Yes = 1;
        Nupp = 1;
    }
    if ((button_hint.contains(mouse) && mouse.getPressed()[0])) {
        Vihje = 1;
        Nupp = 1;
    }
    
    // check that participant has answered all Qs
    if ((Yes == 1)) {
        if (((((RSP_ahhaa.getRating() != null) && (H1_textbox.text != "")) && (RSP_sudden.getRating() != null)) && (RSP_pleasant.getRating() != null))) {
            Valmis = 1;
        }
    } else {
        if ((Vihje === 1)) {
            //if ((((RSP_ahhaa.getRating() != null) && (RSP_sudden.getRating() != null)) && (RSP_pleasant.getRating() != null))) {
            Valmis = 1;
        }
    } 
    
    // continue 
    if ((button_next.contains(mouse_end) && (mouse_end.getPressed()[0] === 1))) {
        mouseIsDown1 = true;
        if ((mouseIsDown1 && (! oldMouseIsDown))) {
            oldMouseIsDown = true;
        }
    } else {
        mouseIsDown1 = false;
    }
    
    // clear brush 
    if ((button_clear.contains(mouse) && (mouse.getPressed()[0] === 1))) {
        mouseIsDown = true;
        buttons, times = mouse.getPressed({"getTime": true});
        location = mouse_track.getPos();
        if ((mouseIsDown && (! oldMouseIsDown))) {
            clear.push(location);
            clear.push(times[0]);
            clear.push("clear");
            brush.reset();
        }
    }
    
    // restart
    if ((mouseIsDown2 === true)) {
        frames += 1;
        if ((frames < 10)) {
            oldMouseIsDown = true;
        } else {
            mouseIsDown2 = false;
            oldMouseIsDown = false;
            frames = 0;
        }
    }
    if ((mouseIsDown1 === true)) {
        frames += 1;
        if ((frames < 10)) {
            oldMouseIsDown = true;
        } else {
            mouseIsDown1 = false;
            oldMouseIsDown = false;
            frames = 0;
        }
    }
    if ((mouseIsDown === true)) {
        frames += 1;
        if ((frames < 10)) {
            oldMouseIsDown = true;
        } else {
            mouseIsDown = false;
            oldMouseIsDown = false;
            frames = 0;
        }
    }
    
    // *juhis_txt* updates
    if (t >= 0.0 && juhis_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      juhis_txt.tStart = t;  // (not accounting for frame time here)
      juhis_txt.frameNStart = frameN;  // exact frame index
      
      juhis_txt.setAutoDraw(true);
    }

    
    // *button_clear* updates
    if (t >= 0.0 && button_clear.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_clear.tStart = t;  // (not accounting for frame time here)
      button_clear.frameNStart = frameN;  // exact frame index
      
      button_clear.setAutoDraw(true);
    }

    
    // *objekt_txt* updates
    if ((Yes == 1) && objekt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      objekt_txt.tStart = t;  // (not accounting for frame time here)
      objekt_txt.frameNStart = frameN;  // exact frame index
      
      objekt_txt.setAutoDraw(true);
    }

    
    // *button_next* updates
    if ((Valmis == 1) && button_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_next.tStart = t;  // (not accounting for frame time here)
      button_next.frameNStart = frameN;  // exact frame index
      
      button_next.setAutoDraw(true);
    }

    // *mouse_end* updates
    if ((Valmis==1) && mouse_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_end.tStart = t;  // (not accounting for frame time here)
      mouse_end.frameNStart = frameN;  // exact frame index
      
      mouse_end.status = PsychoJS.Status.STARTED;
      mouse_end.mouseClock.reset();
      prevButtonState = mouse_end.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_end.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_end.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button_next]) {
            if (obj.contains(mouse_end)) {
              gotValidClick = true;
              mouse_end.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *clear_txt* updates
    if (t >= 0.0 && clear_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      clear_txt.tStart = t;  // (not accounting for frame time here)
      clear_txt.frameNStart = frameN;  // exact frame index
      
      clear_txt.setAutoDraw(true);
    }

    
    // *button_hint* updates
    if (t >= 5.0 && button_hint.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_hint.tStart = t;  // (not accounting for frame time here)
      button_hint.frameNStart = frameN;  // exact frame index
      
      button_hint.setAutoDraw(true);
    }

    if (button_hint.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      button_hint.setAutoDraw(false);
    }
    
    // *vihje_txt* updates
    if (t >= 5.0 && vihje_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      vihje_txt.tStart = t;  // (not accounting for frame time here)
      vihje_txt.frameNStart = frameN;  // exact frame index
      
      vihje_txt.setAutoDraw(true);
    }

    if (vihje_txt.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      vihje_txt.setAutoDraw(false);
    }
    
    // *button_yes* updates
    if (t >= 0.0 && button_yes.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_yes.tStart = t;  // (not accounting for frame time here)
      button_yes.frameNStart = frameN;  // exact frame index
      
      button_yes.setAutoDraw(true);
    }

    if (button_yes.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      button_yes.setAutoDraw(false);
    }
    
    // *leidsin_txt* updates
    if (t >= 0.0 && leidsin_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leidsin_txt.tStart = t;  // (not accounting for frame time here)
      leidsin_txt.frameNStart = frameN;  // exact frame index
      
      leidsin_txt.setAutoDraw(true);
    }

    if (leidsin_txt.status === PsychoJS.Status.STARTED && Boolean(Nupp == 1)) {
      leidsin_txt.setAutoDraw(false);
    }
    
    // *RSP_ahhaa* updates
    if ((Yes == 1) && RSP_ahhaa.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSP_ahhaa.tStart = t;  // (not accounting for frame time here)
      RSP_ahhaa.frameNStart = frameN;  // exact frame index
      
      RSP_ahhaa.setAutoDraw(true);
    }

    
    // *ahhaa_txt* updates
    if ((Yes == 1) && ahhaa_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ahhaa_txt.tStart = t;  // (not accounting for frame time here)
      ahhaa_txt.frameNStart = frameN;  // exact frame index
      
      ahhaa_txt.setAutoDraw(true);
    }

    
    // *RSP_sudden* updates
    if ((Yes == 1) && RSP_sudden.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSP_sudden.tStart = t;  // (not accounting for frame time here)
      RSP_sudden.frameNStart = frameN;  // exact frame index
      
      RSP_sudden.setAutoDraw(true);
    }

    
    // *sudden_txt* updates
    if ((Yes == 1) && sudden_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sudden_txt.tStart = t;  // (not accounting for frame time here)
      sudden_txt.frameNStart = frameN;  // exact frame index
      
      sudden_txt.setAutoDraw(true);
    }

    
    // *RSP_pleasant* updates
    if ((Yes == 1) && RSP_pleasant.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RSP_pleasant.tStart = t;  // (not accounting for frame time here)
      RSP_pleasant.frameNStart = frameN;  // exact frame index
      
      RSP_pleasant.setAutoDraw(true);
    }

    
    // *pleasant_txt* updates
    if ((Yes == 1) && pleasant_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pleasant_txt.tStart = t;  // (not accounting for frame time here)
      pleasant_txt.frameNStart = frameN;  // exact frame index
      
      pleasant_txt.setAutoDraw(true);
    }

    
    // *next_txt* updates
    if ((Valmis == 1) && next_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_txt.tStart = t;  // (not accounting for frame time here)
      next_txt.frameNStart = frameN;  // exact frame index
      
      next_txt.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var KI;
var kk;
function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData(("Version " + vrs.toString()), Version);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_track.x', mouse_track.x);
    psychoJS.experiment.addData('mouse_track.y', mouse_track.y);
    psychoJS.experiment.addData('mouse_track.leftButton', mouse_track.leftButton);
    psychoJS.experiment.addData('mouse_track.midButton', mouse_track.midButton);
    psychoJS.experiment.addData('mouse_track.rightButton', mouse_track.rightButton);
    psychoJS.experiment.addData('mouse_track.time', mouse_track.time);
    
    psychoJS.experiment.addData('H1_textbox.text',H1_textbox.text)
    psychoJS.experiment.addData("mouse1.x_draw", mouse_track.xdraw);
    psychoJS.experiment.addData("mouse1.y_draw", mouse_track.ydraw);
    psychoJS.experiment.addData("Clear pressed", clear);
    
    console.log(clear);
    
    KI = expInfo["Pseudonym*"];
    
    kk = (trials.thisN + 1);
    
    H1_textbox.refresh();
    // store data for psychoJS.experiment (ExperimentHandler)
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('RSP_ahhaa.response', RSP_ahhaa.getRating());
    psychoJS.experiment.addData('RSP_ahhaa.rt', RSP_ahhaa.getRT());
    psychoJS.experiment.addData('RSP_ahhaa.history', RSP_ahhaa.getHistory());
    psychoJS.experiment.addData('RSP_sudden.response', RSP_sudden.getRating());
    psychoJS.experiment.addData('RSP_sudden.rt', RSP_sudden.getRT());
    psychoJS.experiment.addData('RSP_sudden.history', RSP_sudden.getHistory());
    psychoJS.experiment.addData('RSP_pleasant.response', RSP_pleasant.getRating());
    psychoJS.experiment.addData('RSP_pleasant.rt', RSP_pleasant.getRT());
    psychoJS.experiment.addData('RSP_pleasant.history', RSP_pleasant.getHistory());
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var pauseComponents;
function pauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'pause'-------
    t = 0;
    pauseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    brush.reset();
    
    // keep track of which components have finished
    pauseComponents = [];
    pauseComponents.push(text);
    
    pauseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'pause'-------
    // get current time
    t = pauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pauseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pauseRoutineEnd() {
  return async function () {
    //------Ending Routine 'pause'-------
    pauseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(end_txt);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'end'-------
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_txt* updates
    if (t >= 0.0 && end_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_txt.tStart = t;  // (not accounting for frame time here)
      end_txt.frameNStart = frameN;  // exact frame index
      
      end_txt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd() {
  return async function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
