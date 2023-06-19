class Solution:
    def countSmaller(self, nums):
        def merge_sort(arr, indices):
            # Caso base: se o array tem tamanho menor ou igual a 1, retorna o array e os índices
            if len(arr) <= 1:
                return arr, indices

            mid = len(arr) // 2
            # Chama recursivamente o merge_sort para os subarrays esquerdo e direito
            left_arr, left_indices = merge_sort(arr[:mid], indices[:mid])
            right_arr, right_indices = merge_sort(arr[mid:], indices[mid:])

            merged_arr = []
            merged_indices = []
            left_count = 0
            right_count = 0
            inversion_count = 0

            # Combina os subarrays ordenados e conta as inversões
            while left_count < len(left_arr) and right_count < len(right_arr):
                if left_arr[left_count] <= right_arr[right_count]:
                    # Se o elemento no subarray esquerdo é menor ou igual ao elemento no subarray direito, adiciona o elemento e o índice correspondente ao array mesclado
                    merged_arr.append(left_arr[left_count])
                    merged_indices.append(left_indices[left_count])
                    # Incrementa a contagem de inversões para o elemento no subarray esquerdo
                    result[left_indices[left_count]] += inversion_count
                    left_count += 1
                else:
                    # Se o elemento no subarray direito é menor que o elemento no subarray esquerdo, adiciona o elemento e o índice correspondente ao array mesclado
                    merged_arr.append(right_arr[right_count])
                    merged_indices.append(right_indices[right_count])
                    # Incrementa a contagem de inversões para o elemento no subarray direito
                    inversion_count += 1
                    right_count += 1

            # Adiciona os elementos restantes dos subarrays esquerdo e direito
            while left_count < len(left_arr):
                merged_arr.append(left_arr[left_count])
                merged_indices.append(left_indices[left_count])
                # Incrementa a contagem de inversões para os elementos restantes no subarray esquerdo
                result[left_indices[left_count]] += inversion_count
                left_count += 1

            while right_count < len(right_arr):
                merged_arr.append(right_arr[right_count])
                merged_indices.append(right_indices[right_count])
                right_count += 1

            return merged_arr, merged_indices

        result = [0] * len(nums)
        indices = list(range(len(nums)))
        merge_sort(nums, indices)

        return result
