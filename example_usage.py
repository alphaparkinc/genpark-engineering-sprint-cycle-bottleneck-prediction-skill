from client import EngineeringSprintCycleBottleneckPredictionClient

def main():
    client = EngineeringSprintCycleBottleneckPredictionClient()
    res = client.predict_sprint_bottlenecks("sprint_q3_cycle_12", open_pr_count=18, cycle_days_remaining=2)
    print(f"Sprint Completion Probability: {res['sprint_completion_probability_pct']}%")
    print("Rebalancing Action:", res["recommended_workload_rebalancing"])
    print("Isolated Blockers:")
    for b in res["isolated_blockers"]:
        print(f"  - [{b['issue_key']}] {b['title']} (Stalled {b['stalled_hours']}h)")

if __name__ == "__main__":
    main()
