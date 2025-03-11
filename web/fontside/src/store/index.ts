import {nextTick, ref} from "vue";

function useReload() {
    let reloadState = ref(true);

    function reloadPage() {
        reloadState.value = !reloadState.value;
        nextTick(() => {
            reloadState.value = !reloadState.value;
        })
    }

    return {reloadState, reloadPage};
}

const {reloadState, reloadPage} = useReload();

export {
    reloadState,
    reloadPage,
}