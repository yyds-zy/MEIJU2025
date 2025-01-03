set -e
gpu=$1



# --input_dim_a=512 --embd_size_a=128 --embd_method_a=maxpool
# --input_dim_v=342 --embd_size_v=128  --embd_method_v=maxpool
# --input_dim_l=768


# cmd="python test_baseline.py --model=our
# --checkpoints_dir=./checkpoints --gpu_ids=$gpu
# --input_dim_a=768 --embd_size_a=128 --embd_method_a=maxpool
# --input_dim_v=256 --embd_size_v=128  --embd_method_v=maxpool
# --input_dim_l=768 --embd_size_l=128  --hidden_size=128
# --A_type=wav2vec2-base-960h-UTT --V_type=temonet_UTT --L_type=roberta-base-4-FRA
# --num_thread=8 --corpus=MEIJU_English
# --emo_output_dim=7 --int_output_dim=8 --track=2
# --cls_layers=128,64 --dropout_rate=0.2 --use_ICL=True
# --batch_size=32 --lr=2e-4 --weight_decay=1e-5
# --name=pretrain_English_run_0,1,2,3_1
# --cvNo=1"

cmd="python test_baseline.py --model=our
--checkpoints_dir=./checkpoints --gpu_ids=$gpu
--input_dim_a=768 --embd_size_a=32 --embd_method_a=maxpool
--input_dim_v=342 --embd_size_v=128  --embd_method_v=maxpool
--input_dim_l=768 --embd_size_l=128  --hidden_size=128
--A_type=wav2vec2-base-960h-UTT --V_type=temonet_UTT --L_type=roberta-base-4-FRA
--num_thread=8 --corpus=MEIJU_English
--emo_output_dim=7 --int_output_dim=8 --track=2
--cls_layers=128,64 --dropout_rate=0.2 --use_ICL=True
--batch_size=32 --lr=2e-4 --weight_decay=1e-5
--name=pretrain_English_run_0,1,2,3_1
--cvNo=1"




echo "\n-------------------------------------------------------------------------------------"
echo "Execute command: $cmd"
echo "-------------------------------------------------------------------------------------\n"
echo $cmd | sh

