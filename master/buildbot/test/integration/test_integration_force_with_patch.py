    @defer.inlineCallbacks
    def run_vc(self, branch, revision, patch):
        self.stdio_log = yield self.addLogForRemoteCommands("stdio")
            yield self.patch(patch)
        return SUCCESS
        build = yield self.doForceBuild(wantSteps=True, wantLogs=True,
                                        forceParams={'foo_patch_body': PATCH})
        self.assertEqual(build['steps'][1]['results'], SUCCESS)
        self.assertEqual(build['steps'][2]['results'], FAILURE)