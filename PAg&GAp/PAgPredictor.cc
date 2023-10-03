#include "cpu/pred/PAgPredictor.hh"

#include "base/intmath.hh"
#include "base/logging.hh"
#include "base/trace.hh"
#include "debug/Fetch.hh"

namespace gem5
{

namespace branch_prediction
{

PAgPred::PAgPred(const PAgPredParams &params)
    : BPredUnit(params),
    lhistoryWidth(params.lhistoryWidth),
    ltableHeight(params.ltableHeight),
    gtableHeight(params.gtableHeight),
    gpredSize(params.gpredSize),
    nbit_counters(params.gtableHeight, SatCounter8(params.gpredSize)) ,//vector with gtableHeight elements type SatCounter8 predictors of n bits
    local_history_table(params.ltableHeight,0) //initialize local table with 0 values 
      // more parameters are needed to be passed here, check BranchPredictor.py
{
    // you may want to add some checks of the passed parameters here
    if (!isPowerOf2(lhistoryWidth)) {
        fatal("Invalid local history width size!\n");
    }

    if (!isPowerOf2(ltableHeight)) {
        fatal("Invalid local table height size!\n");
    }

    if (!isPowerOf2(gtableHeight)) {
        fatal("Invalid global table height size!\n");
    }

    if(log2(gtableHeight)!=lhistoryWidth){
        fatal("Local history width must be equal to log2(gtableheight) for indexing!");
    }
}

// unused
void
PAgPred::btbUpdate(ThreadID tid, Addr branch_addr, void * &bp_history)
{
   
// Place holder for a function that is called to update predictor history when
// a BTB entry is invalid or not found.
}

bool
PAgPred::lookup(ThreadID tid, Addr branch_addr, void * &bp_history)
{
    // implement the lookup logic here
    bool taken ;
    unsigned local_index = get_local_index(branch_addr);
    unsigned global_index = get_global_index(local_index);
    uint8_t predictor = nbit_counters[global_index];
    taken = prediction(predictor);
    return taken;
    
}

void
PAgPred::update(ThreadID tid, Addr branch_addr, bool taken, void *bp_history,
                bool squashed, const StaticInstPtr & inst, Addr corrTarget)
{
    // implement the update logic here
    unsigned local_index = get_local_index(branch_addr);
    unsigned global_index = get_global_index(local_index);
    if(taken){
        nbit_counters[global_index]++;
        
    }else{
        nbit_counters[global_index]--;
        //
    }
    local_history_table[local_index]=(local_history_table[local_index]<<1)|taken; 
}

// unused
void
PAgPred::uncondBranch(ThreadID tid, Addr pc, void *&bp_history)
{
}

}

}
