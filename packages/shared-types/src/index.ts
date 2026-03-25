export interface ProjectHealth {
  status: "ok" | "degraded" | "error";
  project: string;
}
