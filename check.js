const fs=require('fs'),vm=require('vm');
const source=fs.readFileSync(__dirname+'/game.js','utf8');
const test={
  querySelector(s){return s==='#app'?this.app:{textContent:'',classList:{add(){},remove(){}},innerHTML:''}},
  app:{innerHTML:'',addEventListener(){}}
};
const store=new Map();
const ctx={document:test,window:{speechSynthesis:undefined,scrollTo(){},matchMedia(){return {matches:true}}},localStorage:{getItem:k=>store.get(k),setItem:(k,v)=>store.set(k,v)},SpeechSynthesisUtterance:undefined,matchMedia:()=>({matches:true}),setTimeout(fn){},clearTimeout(){},Math,Date,console};
vm.createContext(ctx);vm.runInContext(source,ctx);
function js(v){return vm.runInContext(v,ctx)}
console.log('letters',js('LETTERS.length'),'vowels',js('VOWELS.length'),'words',js('VOCAB.length'),'numbers',js('NUMBERS.length'),'phrases',js('PHRASES.length'),'worlds',js('WORLDS.length'),'levels',js('ALL_LEVELS.length'));
let failures=[];
for (const tier of [3,6,8]){
  js(`saved.age=${tier}`);
  for(let i=0;i<js('WORLDS.length');i++){
    const w=js('WORLDS')[i];
    for(let j=0;j<w.items.length;j++){
      js(`activeWorld='${w.id}';activeLevel=${j}`);
      const types=js('quizTypes(item())');
      for(const t of types){const q=js(`mkQuestion('${t}',item())`);if(q.trace)continue;
        const counts=q.options.filter(o=>o.value===q.correct).length;
        if(counts!==1)failures.push({tier,world:w.id,level:j,type:t,correctCounts:counts,options:q.options.map(o=>o.value)});
        if(q.options.some(o=>o.value===undefined))failures.push({tier,world:w.id,level:j,type:t,undefinedOption:true});
      }
    }
  }
}
console.log('question issues:',failures.length,failures.slice(0,15));
if(failures.length)process.exitCode=1;