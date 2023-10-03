#include "cpu/pred/GApPredictor.hh"

#include "base/intmath.hh"
#include "base/logging.hh"
#include "base/trace.hh"
#include "debug/Fetch.hh"

namespace gem5
{

namespace branch_prediction
{

GApPred::GApPred(const GApPredParams &params)
    : BPredUnit(params),
    historySize(params.historySize),
    ptableHeight(params.ptableHeight),
    ptableWidth(params.ptableWidth), 
    predSize(params.predSize),
    ptable(params.ptableHeight,std::vector<SatCounter8>(params.ptableWidth,SatCounter8(params.predSize))),
    history(params.historySize,0)
      // more parameters are needed to be passed here, check BranchPredictor.py
{
    // you may want to add some checks of the passed parameters here
      if (!isPowerOf2(ptableHeight)) {
        fatal("Invalid predictor table height size!\n");
    }

    if (!isPowerOf2(ptableWidth)) {
        fatal("Invalid predictor table width size!\n");
    }

    if (!isPowerOf2(ptableHeight)) {
        fatal("Invalid global table height size!\n");
    }

   if(log2(ptableHeight)!=historySize){
        fatal("history size must be equal to log2(ptableheight) for indexing!");
   }
   

}

// unused
void
GApPred::btbUpdate(ThreadID tid, Addr branch_addr, void * &bp_history)
{
// Place holder for a function that is called to update predictor history when
// a BTB entry is invalid or not found.
}

bool
GApPred::lookup(ThreadID tid, Addr branch_addr, void * &bp_history)
{
    // implement the lookup logic here
    unsigned row_idx = get_row_index();
    unsigned col_idx = get_col_index(branch_addr);
    uint8_t predictor = ptable[row_idx][col_idx];
    return prediction(predictor);
    
}

void
GApPred::update(ThreadID tid, Addr branch_addr, bool taken, void *bp_history,
                bool squashed, const StaticInstPtr & inst, Addr corrTarget)
{
    // implement the update logic here
    unsigned row_idx = get_row_index();
    unsigned col_idx = get_col_index(branch_addr);
    if(taken){
        ptable[row_idx][col_idx]++;
    }
    else{
        ptable[row_idx][col_idx]--;
    }
    history.push_back(taken);
}

// unused
void
GApPred::uncondBranch(ThreadID tid, Addr pc, void *&bp_history)
{
}

}

}
